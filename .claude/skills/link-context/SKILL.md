---
name: link-context
description: Make a new file, folder, project, or online source findable in the business workspace by adding a verified route to the appropriate context or source index. Use when adding context or asking the AI to remember where information lives.
---

Read AGENTS.md and the relevant existing index. Resolve workspace paths from the project root. Identify the target and its intended use from the request; ask one concise question only when either is unclear.

Inspect the target using available authorized tools. Check that a local path resolves, or that an online source can actually be read. A public URL may still block access. Do not install a connector, widen permissions, or copy private content just to register a source. If access is unavailable, record the exact reference as unverified with its blocker; never claim it was tested successfully.

Choose the smallest useful route:
- Business context files belong in context/index.md, with a brief explanation of when to read them.
- External tools, source folders, meetings, channels, and reference material belong in sources/index.md, with purpose, business scope, location, access method, verification date, and limitations.
- Project-specific material belongs in the project's existing index, with one route from the business index if needed.

Reuse canonical indexes and update an existing entry rather than duplicating it. Prefer relative paths for files within the workspace, and durable links or service identifiers for online sources. Do not move originals or bulk-import content unless requested. Linking a source does not make everything in it a confirmed current business fact. Keep old-company material, client work, and tentative plans scoped explicitly.

Retain access boundaries: a registered source is not permission for ongoing monitoring or unrelated reads. Keep secrets and private source indexes out of public commits. Do not change strategy, customer avatar, or products while merely registering a source.

After saving, follow the new route from the index and verify that it identifies the intended target. Report the index updated, what the source is useful for, and whether access is verified or blocked. If the target cannot be resolved, leave existing working routes intact and explain the limitation.
