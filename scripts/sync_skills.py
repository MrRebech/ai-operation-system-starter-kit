"""Generate Claude discovery copies from the canonical starter and custom skills."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
source = root / '.agents' / 'skills'
destination = root / '.claude' / 'skills'
for skill in sorted(source.iterdir()):
    if skill.is_dir() and (skill / 'SKILL.md').is_file():
        target = destination / skill.name
        target.mkdir(parents=True, exist_ok=True)
        # Merge managed files without deleting unrelated user resources.
        shutil.copytree(skill, target, dirs_exist_ok=True)
        print(f'Synchronized {skill.name}')
