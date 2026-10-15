# Setup readiness rubric v1

Adapted from Nate Herk's AIS-OS audit. This is a starter-kit rubric, not an identical implementation of his scoring. Use four equally weighted categories, five criteria each, maximum five points per criterion: 100 points total.

Score each criterion using evidence:
- **0:** checked and missing, broken, contradicted, or unsafe.
- **1:** stated or documented, but usable execution or retrieval is unproven.
- **3:** works in a relevant check, with known coverage or reliability gaps.
- **5:** verified for its intended scope, with clear ownership, reliable retrieval or repeated success, and no material unresolved gap.
- **null:** not assessed. A blocked current read may be assessed as unverified (0 or 1 with evidence); a skipped check is null.

Every score requires a source/path, observation, date, and reason. Use the highest level fully supported, not an average of optimistic guesses. Do not award points for installing more tools or writing more files.

## Context /25
C1. Current business, offer, customer, and goals are specific, coherent, and sourced.
C2. All five retrieval probes recover the intended current information through documented routes.
C3. Canonical ownership, source authority, scope, dates, and conflicts are clear.
C4. Brand assets, writing voice, restrictions, and working preferences are usable and consistent.
C5. Learning survives sessions: captures, corrections, resume points, and confirmed updates are saved and findable.

## Connections /25
N1. The selected sources match real business needs and have precise routes and access scope.
N2. Minimal current authorized reads succeed for priority sources.
N3. Credentials and permissions are handled safely, with no tracked secrets or excessive grants.
N4. Denied access, stale sources, and failures are surfaced honestly with a usable fallback.
N5. Source use is repeatable and traceable to the relevant records; large bulk imports are unnecessary.

Read-only access can earn full marks when it meets the intended work. A deliberately local-only setup can satisfy connection criteria through verified local inputs and documented local boundaries. Do not push users to connect unnecessary services. A listed integration or API-key field alone earns no execution evidence.

## Capabilities /25
W1. Up to three priority workflows have clear inputs, outputs, owners, and acceptance criteria.
W2. Existing outputs show those workflows perform useful work correctly.
W3. Relevant context, brand, voice, and tools are applied consistently.
W4. Approval boundaries, failure behavior, and recovery are explicit and demonstrated where possible without new side effects.
W5. Workflows can be resumed or repeated in the configured runtime, with evidence from more than one real use.

No workflows defined means checked missing criteria, not five imaginary successes. Do not run a new workflow merely to inflate the audit.

## Cadence /25
R1. Recurring work has an agreed trigger, owner, and scope.
R2. Due runs have actually completed and produced usable results.
R3. Run history and failure signals are available to the owner.
R4. Pause/stop controls, duplicate prevention, and recovery match the work's risk.
R5. Context, permissions, and workflows receive documented maintenance.

Manual routines count, but cap this category at 10/25 if all routines rely on someone remembering to start them. Do not create automation to raise the score. Report manual operation as a conscious scope choice where applicable.

## Calculation and guardrails
Sum the criteria. If C1 or C2 is zero, cap Context at 10/25 because the business foundation or retrieval is missing. Apply this and the cadence cap before total caps. If N3 or W4 is zero, cap the overall score at 49 because credential or action safeguards are missing. The strictest total cap wins:
- If any category is below 10: maximum 49/100.
- If any category is below 15, or fewer than two successful due automatic runs are evidenced: maximum 69/100.
- If any category is below 20, or a material unresolved conflict exists: maximum 84/100.
- Otherwise the sum may reach 100.

Record every applied cap and the uncapped sum. If a category is not assessed, the overall score is null. Do not silently change weights or drop categories to make a partial audit look complete. A setup may be useful for manual work while scoring below full operational readiness.

Use scripts/score_setup.py from the repository root to calculate arithmetic from an evidence-backed assessment JSON. Input keys: categories (context, connections, capabilities, cadence), each an array of five objects with score and evidence; manual_only (boolean), successful_due_runs (nonnegative integer), material_conflict (boolean). Evidence is a nonempty string for assessed criteria. Never put credentials in this file. The script checks inputs and calculates totals; it does not validate the truth of evidence.

Compare only the same rubric version and scope. Explain whether change came from actual repairs, new evidence of existing behavior, or different coverage. No promised increase after Bridge the Gaps.
