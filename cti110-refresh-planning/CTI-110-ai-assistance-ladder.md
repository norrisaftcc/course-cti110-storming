# CTI 110 — AI Assistance Ladder (Companion Doc)

**Why this doc exists:** The course opens (Module Zero) by confronting "why not just let the AI do it?" and closes (Module Eight) by *permitting* AI assistance. That arc is pedagogy, not inconsistency — but only if the policy is explicit, per-module, and explained in terms students can respect. An unstated policy reads as arbitrary; a stated ladder reads as training.

**The one-sentence version for students:**
> You may use AI exactly to the degree that you can verify its output — and this course exists to build that verification ability.

---

## The Ladder

| Rung | Policy | Modules | Rationale (stated to students) |
|---|---|---|---|
| 0 | **AI as topic, not tool.** We discuss it; we don't use it for coursework. | M0 | You can't evaluate a tool for a job you don't understand yet. |
| 1 | **No AI on artifacts.** Instructions, markup, flowcharts, and user stories are written by you. | M1–M2 | These modules *are* the skill AI can't supply: knowing and stating what you want. Outsourcing them is skipping the course. |
| 2 | **AI as explainer, not author.** You may ask AI to explain an error message or a concept. You may not submit code it wrote. | M3–M5 | Reading explanations builds the verification muscle. Submitting generated code while learning syntax is lifting with a forklift. |
| 3 | **AI as reviewer.** After your solution works, you may ask AI to critique it. Improvements must be understood and documented (brief note: what changed and why). | M6–M7 | This mirrors professional code review — and forces the "did it even understand the problem?" check from Module Zero. |
| 4 | **AI as collaborator.** Full assistance permitted for implementation. Problem formulation, spec, and presentation are yours, and are graded heavily. | M8 | This is the real-world configuration. We grade what AI can't do for you: defining the problem and standing behind the result. |

---

## Enforcement Philosophy

- **Design over detection.** The rungs are enforced primarily by assignment design (spec-first gates, in-class traces, presentations with live Q&A), not by AI-detection tooling, which is unreliable and adversarial.
- **Copilot: norms and settings, not lockdown.** New students frequently find autocomplete *confusing* rather than tempting ("what is this, how do I stop it"). Early modules explicitly show how to disable Copilot/inline suggestions and explain why they'll want it off while building fundamentals — and that it will be welcomed back at Rung 4. Students who then choose to violate clear academic policy have made a documented choice; that is an academic-integrity matter, not a course-design failure.
- **The presentation is the audit.** In M8, a student who cannot explain their own software fails the presentation regardless of whether the software runs. This is stated up front.
- **Disclosure is normalized, not confessional.** From Rung 3 onward, "what AI helped with" is a standard line item in submissions — the habit of attribution, framed as professional practice.

---

## Connection to Workforce Framing

Employers in the current market are not hiring "people who can prompt." They are hiring people who can:
1. Formulate a problem precisely (M1–M2, graded at Rung 1 with no AI cover),
2. Verify that a solution — human- or AI-authored — actually solves it (M3–M7, the verification muscle),
3. Take responsibility for shipped work (M8 presentation).

The ladder is the workforce argument from Module Zero, operationalized: *even if your plan is to have AI do the work, you must climb the rungs to be the person allowed to supervise it.*

---

## Open Questions

1. Should Rung 2 permit AI-generated *practice problems* (student asks for extra exercises)? Low risk, arguably beneficial — recommend yes, with the caveat that generated exercises aren't vetted.
2. Does the department want a shared disclosure template (one paragraph: tools used, what for, what was changed)? Reusable in CSC 121/221 and the capstones for continuity.
3. Alignment upstream: does this ladder's Rung 4 match the AI policy already in use in the CSC 289 capstone, so students see one coherent institutional stance?
