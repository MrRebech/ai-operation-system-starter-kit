# AI Operation System Starter Kit

A simple starting point for business owners using an AI agent with local files and tools.

## Start here
Download and extract this repository into a new folder. Open that folder in Codex, Claude Code, Hermes, or another capable agent. Send:

> Read START-HERE.md and start my onboarding.

Sharing a repository link works only if your agent can fetch it and create a local workspace. A clone or download alone does not launch a conversation. Never paste passwords or API keys into the interview.

The agent asks seven questions, researches the sources you choose, and saves a business brief plus reusable business context. It creates a brand PDF when its environment supports PDF generation. You can pause and resume.

## Included workflows
- **Onboard:** seven questions followed by focused research and your first business brief.
- **Bridge the Gaps:** request five to ten questions, one at a time, to improve unclear context after onboarding.
- **Link Context:** make a new file, folder, project, or source easy to find again.
- **Check My Setup:** verify files, retrieval, and actual tool access with a short actionable report.

Codex discovers `.agents/skills/`; Claude copies can be generated with `python scripts/sync_skills.py`. Other agents can read those same skill files directly through START-HERE.md. Tool authentication, native skill discovery, and scheduling vary by agent; no universal connector installation is promised.

New chats must open this workspace and load its operating instructions to use the saved context. This does not install global memory across unrelated chats.

## Private by default
Personal context, uploads, interviews, reports, and custom skills are gitignored. Keep your working copy private and review staged files before publishing. The public template contains no Kenneth-specific business data, credentials, or connected accounts.

## Design
Four focused starter skills. No required subscription beyond the agent and services you choose. No bundled autonomous agents or scheduled jobs. Add reusable skills after a useful workflow succeeds.

Inspired by the business-context starter-kit approach in Nate Herk's AIS-OS: https://github.com/nateherkai/AIS-OS. This starter uses its own onboarding, wording, and workflows; it does not include Nate's branded frameworks or source files.

## License and credit
Created by **Kenneth Rebech**. Licensed under [MIT](LICENSE). If you redistribute copies or substantial portions, retain the copyright and license notice. See [credit and reuse guidelines](ATTRIBUTION.md) for required notices and suggested public credit.
