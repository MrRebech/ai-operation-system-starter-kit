# Begin setup

Read AGENTS.md, then `.agents/skills/onboard/SKILL.md`. When the user asks to set up this starter, begin the interview immediately, one question at a time. Do not ask a preliminary permission question.

If received as a repository URL, fetch the files into a new local workspace using the tools available. Preserve any existing project and its instructions. If you cannot fetch files or write locally, explain that a file-capable agent is required; do not claim installation succeeded.

No account connections are supplied by this repository. Discover the current agent's available tools, and guide the user through its supported authentication when needed. Obtain access through the service's normal secure flow.

Other workflows, when requested:
- Link Context: `.agents/skills/link-context/SKILL.md`
- Bridge the Gaps: `.agents/skills/bridge-the-gaps/SKILL.md`
- Check My Setup: `.agents/skills/check-my-setup/SKILL.md`

The canonical skills live under `.agents/skills/`. For Claude's native skill discovery, run `python scripts/sync_skills.py` when Python is available. Without Python, copy those skill folders into `.claude/skills/`. For other agents, follow their installed version's discovery conventions or read the canonical files directly. Never assume a copied skill is automatically discovered.
