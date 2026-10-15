"""Add empty credential fields to an ignored local .env; never print values."""
import os
import re
import subprocess
import sys
from pathlib import Path

def prepare(root, names):
    root = Path(root).resolve()
    if not names or any(not re.fullmatch(r"[A-Z][A-Z0-9_]*", n) for n in names):
        raise ValueError("Supply uppercase variable names only, never keys or values.")
    path = root / ".env"
    if path.is_symlink():
        raise ValueError("Refusing a linked .env file.")
    def git(*args):
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    tracked = git("ls-files", "--error-unmatch", "--", ".env")
    ignored = git("check-ignore", "-q", "--", ".env")
    if tracked.returncode == 0 or ignored.returncode != 0:
        raise ValueError(".env must be untracked and gitignored before setup.")
    # Read privately in this process. Never return file contents or values.
    data = path.read_bytes() if path.exists() else b""
    existing = set(re.findall(rb"(?m)^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=", data))
    missing = list(dict.fromkeys(n for n in names if n.encode() not in existing))
    if missing:
        newline = b"\r\n" if b"\r\n" in data else b"\n"
        addition = (newline if data and not data.endswith(b"\n") else b"")
        addition += newline.join(n.encode() + b"=" for n in missing) + newline
        if path.exists():
            with path.open("ab") as stream:
                stream.write(addition)
        else:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as stream:
                stream.write(addition)
    return missing

if __name__ == "__main__":
    try:
        added = prepare(Path(__file__).resolve().parents[1], sys.argv[1:])
        print("Added empty fields: " + ", ".join(added) if added else "Existing fields preserved.")
        print("Open the local .env file to enter values. Never paste secrets in chat.")
    except (ValueError, OSError) as error:
        # Do not expose credential contents or raw subprocess errors.
        print(str(error) if isinstance(error, ValueError) else "Could not safely prepare .env.", file=sys.stderr)
        sys.exit(1)
