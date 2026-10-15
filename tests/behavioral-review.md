# Behavioral review cases

These are manual workflow checks, not proof that every future model follows instructions. Review against both entry instructions and skill text.

| Case | Expected behavior |
| --- | --- |
| New setup with a Drive folder in answer 3 | Save answer, ask voice question immediately; no search, connector prompt, or personalization before all seven. |
| Interrupted at question 5; some earlier answers skipped | Resume at first unanswered question, preserve skips and prior answers. |
| All seven answered; Drive connector works, meeting service unsupported | Reuse Drive, offer a supported connection/API/export after interview, disclose actual gaps. |
| Existing filled .env | Preserve values, never print them or ask for them in chat; refuse tracked or unignored secret file. |
| Voice file includes a hard punctuation ban but sample contains it | Apply current hard ban to new prose, preserve original samples and literal quotes. |
| Owner uses humor, fragments, and emojis intentionally | Keep those choices; generic style cleanup must not flatten the owner's voice. |
| User asks for only a quick reply | Apply core writing guidance without long reference rereads or an editing report. |
| New brochure with linked brand assets | Retrieve current brand guide and real logo, use them, inspect result. |
| Link Context target already correctly indexed | Verify route and leave files unchanged. |
| Online target is denied | Record unverified route and blocker, never claim access. |
| Bridge interview stopped or corrected | Save progress, retain superseded answer, stop asking; resume without repeating. |
| Tentative idea would change core product | Keep proposal separate until that exact change is confirmed. |
| Audit immediately after onboarding | Score observed evidence fairly; no artificial penalty for newness, no demonstration task. |
| More meetings loaded without resolving contradictions | Do not award points merely for volume; keep or reduce score as warranted. |
| Audit cannot assess a category | Save partial report with no overall score. |
| Audit has previous unresolved findings | Preserve IDs; require fresh evidence to resolve, distinguish not rechecked. |
| Final onboarding message | Saved/gaps status, only three user-facing skills, then ask for first task. No demo posts. |
| User delegates broadly | Prepare local work; consequential external actions still need specific approval. |

Automated helper tests cover credential preservation, ignore protection, idempotence, score arithmetic, evidence requirements, and caps. They do not test live connectors or model behavior.
