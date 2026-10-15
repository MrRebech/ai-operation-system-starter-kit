# AI Operation System Starter Kit

A starting point for business owners who want an AI agent to understand their business and do useful work.

## Start here
Download this repository into a new folder. Open it in a file-capable agent and say:

> Read START-HERE.md and start my onboarding.

A repository link also works when your agent can fetch it into a workspace. Downloading files alone does not start a conversation.

The agent asks seven quick questions: business, customer, context, voice, brand, working style, and direction. Research and connection setup happen after the questions. It saves your answers so you can pause and resume. Once your context is saved, you choose the first task. No sample posts or demo work are required.

## Available skills
- **Bridge the Gaps:** Asks focused questions to fill missing information and clear up confusion about your business.
- **Link Context:** Records where new files, folders, and sources live, what they contain, and when the AI should use them.
- **Check My Setup:** Checks your context, access, workflows, and operating routines. Gives an evidence-based score out of 100 and up to three useful next steps.

Your brand, voice, writing restrictions, and communication preferences guide future work. Natural-writing guidance runs automatically. It preserves your style and explicit rules.

## Private by default
Never share API keys, passwords, or confidential information in chat. Use supported secure connection flows. When an API is a usable fallback, the agent prepares an ignored local `.env` file and shows where to enter the key. `.env.example` contains empty examples only. Accounts and connectors are not bundled.

Business context, assets, interviews, reports, outputs, and custom skills are gitignored. Review staged files before publishing. The template contains no owner's private business data. Consequential external actions require approval unless the user has given clear, scoped standing permission.

## How it works
Canonical skills live in `.agents/skills/`. Claude discovery copies are included in `.claude/skills/`; update them with `python scripts/sync_skills.py` after editing. Other agents can read START-HERE.md and the skill files directly. Native discovery, authentication, and scheduling depend on the host.

New chats must open this workspace and load its instructions. This does not create global memory across unrelated chats. The kit installs no scheduled jobs. A setup score reflects verified readiness, not the volume of uploaded material or a guarantee of correctness.

## Maintenance
Run `python -m unittest discover -s tests -v` for the credential-file and scoring checks. Review the behavioral cases in [tests/behavioral-review.md](tests/behavioral-review.md) when changing the workflows. Keep both skill copies synchronized.

## License and credits
[MIT License](LICENSE). Copyright 2026 Kenneth Rebech. The interview, linking, and audit workflows adapt ideas from Nate Herk's AIS-OS. Natural-writing guidance adapts his Human Speak project. See [ATTRIBUTION.md](ATTRIBUTION.md) and [LICENSES](LICENSES) for upstream notices.
