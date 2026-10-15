# Report history

Save each requested audit in a new timestamped file with a random suffix under reports/setup-checks/. Use exclusive creation or verify a unique path; never overwrite a prior report. If saving fails, report that limitation and provide findings in chat. Respect an explicit request not to save.

Report fields:
- Timestamp, workspace, runtime, scope, rubric version, report path, baseline report if comparable.
- Overall score or null for partial work, raw sum, category scores, applied caps.
- Each criterion: score, evidence path/source, observation date, reasoning, and confidence limits.
- Five retrieval probes and actual source-read outcomes.
- Findings with stable IDs, impact, evidence, and status.
- Up to three recommended fixes, with the useful outcome each enables.
- Comparison explaining actual changes, newly verified evidence, and coverage differences.

Carry finding IDs forward. Statuses: new, still open, resolved, reopened, not rechecked, no longer applicable. Resolve only with fresh supporting evidence. A missing finding in a new report is not proof it was fixed. Never reinterpret old reports under a new rubric without clearly labeling a separate reassessment.
