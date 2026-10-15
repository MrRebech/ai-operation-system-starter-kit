# Begin setup

Read AGENTS.md, then `.agents/skills/onboard/SKILL.md`. For a setup request, begin immediately with the first unanswered question. Do not ask permission to start.

If received as a repository URL, fetch it into a new local workspace with available tools, preserving existing projects and instructions. A download alone does not launch a conversation. If you cannot fetch or save files, explain that a file-capable agent is needed; do not claim installation succeeded.

Keep the interview fast. Save each answer in one small checkpoint and ask the next question. No web research, account setup, folder inspection, brand work, or generated samples between questions. After all seven, connect the selected sources, research, and save the foundation.

Skills live in `.agents/skills/`. The repository includes Claude discovery copies in `.claude/skills/`; after edits, run `python scripts/sync_skills.py` if Python is available. Otherwise copy the changed skills and their references. Other agents should read the canonical skills directly or follow their supported discovery conventions. Do not assume discovery or tool access works because files exist.

No account connections or scheduled jobs are supplied. Use the host's supported secure connection flow only after the interview. Never ask for secrets in chat.
