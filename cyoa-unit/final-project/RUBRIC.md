# Final Project Rubric

CTI 110, Fall 2026 · Spine module M8 · 100 points

**Formulation plus presentation = 65.** The blueprint (35) and the presentation (30) are 65 of the 100 points, as the course spine asks for M8 and as the AI Ladder says for Rung 4: "Problem formulation, spec, and presentation are yours, and are graded heavily." AI may help with the build. It may not help with the parts that carry most of the grade.

| Part | Points |
|---|---|
| A. Blueprint (formulation) | 35 |
| B. Build | 15 |
| C. Verification | 15 |
| D. Presentation | 30 |
| E. AI disclosure and `prompts.md` | 5 |
| **Total** | **100** |
| Extra credit: stretch effects | up to +3 |

Each row has three levels. **Meets** earns the full points. **Partly** earns the points shown. **Not yet** earns the low number shown. A grader may give a number in between when the work falls between two levels.

---

## A. Blueprint (35 points)

Graded on `stories/blueprint.md` and `stories/story.json` as handed in at the gate, Tue 11/24/26. Written by you, with no AI.

| Row | Meets | Partly | Not yet |
|---|---|---|---|
| **A1. User stories with Given/When/Then and checks** (12) | **12.** 3 to 6 user stories, each in the form "As a player, I want ..., so that ...". Each has a Given/When/Then that names a real scene, choice or ending. Each has a check that names a checker line or a golden-run file. At least one story is about the lever. | **6.** The stories are there, but one or two criteria are vague ("it works", "it is fun"), or one or two checks name nothing that exists. | **0 to 2.** Fewer than 3 stories, or no Given/When/Then, or no checks. |
| **A2. The Mermaid map matches `story.json`** (8) | **8.** It renders on GitHub. Every scene is a box and every ending is a rounded box. Every `to`, `next`, `ending` and `route` exit is an edge. Each edge label is the option label, with its condition in parentheses. | **4.** It renders, but one to three scenes or edges are missing, extra, or point the wrong way. | **0.** Missing, does not render, or shows a different story. |
| **A3. `story.json` passes the checker** (10) | **10.** `python3 checker.py stories/story.json` prints `RESULT: PASS` at the start of class. 6 to 15 scenes and at least 3 endings, with no rule 20 warning. A flag opens a choice. | **5.** It passes only after a fix made in class on gate day, or it has a rule 20 warning, or no flag opens a choice. | **0.** `RESULT: FAIL`, or no `story.json`. |
| **A4. The cut list and the lever** (5) | **5.** The cut list has at least 3 rows, each with a reason and a "revisit when". The lever section names the field (`role`), where it is set, its values, what each value opens, and why it matters. | **2 to 3.** One of the two is thin: fewer than 3 cuts, a cut with no reason, or a lever that opens options but does not say why it matters. | **0.** No cut list, or no lever section. |

---

## B. Build (15 points)

Graded on the turned-in repository. AI may help here (Rung 4).

| Row | Meets | Partly | Not yet |
|---|---|---|---|
| **B1. The feature works and sits outside the frozen files** (10) | **10.** The feature does what its user story (US-F) says, and its check passes. It lives in `game.py`, a `display_*.py` file or a new `.py` file. `engine.py`, `checker.py` and `tests/run_tests.py` are unchanged: the checker does not warn that `engine.py` has changed. | **5.** The feature works in part, or it works but has no US-F or no check. | **0.** It does not work, or a frozen file was changed. |
| **B2. Readable code** (5) | **5.** Every file you wrote or changed has the class header. The feature is in small functions with names that say what they do. Each function has a one-line comment or docstring. No `class`, no `global`. | **2 to 3.** Works, but one long function, or names like `x` and `thing`, or the header is missing. | **0.** Cannot be read by a classmate. |

---

## C. Verification (15 points)

| Row | Meets | Partly | Not yet |
|---|---|---|---|
| **C1. Golden runs pass for every claimed ending** (8) | **8.** One `tests/story_<ending id>.in` and `.out` pair for each ending you claim, at least 3. Each `.in` has the header `# story: stories/story.json seed: N`. Each `.out` ends at the ending its name says. All pass. | **4.** Fewer pairs than endings claimed, or one `.out` ends somewhere other than its name says. | **0.** No golden runs, or none pass. |
| **C2. Peer playtest, with one fix or note** (4) | **4.** The playtest form is signed by a classmate who reached at least 2 endings. It names one confusing spot. You made one fix (a commit) or wrote a note on why you did not. | **2.** The form is signed, but no fix and no note. | **0.** No form. |
| **C3. `run_tests.py` passes** (3) | **3.** `python3 tests/run_tests.py` prints `ALL TESTS PASSED` on the turned-in repository. | **1.** One test fails, and your blueprint notes say which one and why. | **0.** Tests fail with no note, or the runner crashes. |

---

## D. Presentation (30 points)

5 minutes, then questions. Tue 12/8/26 or Thu 12/10/26.

**A student who cannot explain their own software fails the presentation.** That student earns 0 of the 30 points in part D, even if the game runs. "Explain" means: say what a part does and why it is there, in your own words.

| Row | Meets | Partly | Not yet |
|---|---|---|---|
| **D1. Plays live** (8) | **8.** Runs from your own repository. Plays one path to an ending. Names the lever when you choose it. | **4.** It runs only with help, or it crashes and you recover. | **0.** It does not run. |
| **D2. Explains the map and one user story with its check** (8) | **8.** Shows the Mermaid map and walks one path on it. Reads one user story with its Given/When/Then. Shows its check passing (the checker line, or the golden run in `run_tests.py`). | **4.** Shows the map and the story, but cannot show the check, or the check does not match the story. | **0.** No map or no story shown. |
| **D3. Explains one line of the build feature** (8) | **8.** Picks one line of the feature. Says what it does, why it is there, and what would break without it. | **4.** Says what the line does, but not why. | **0.** Cannot explain a line of the feature. |
| **D4. Questions** (6) | **6.** Answers two or more questions in your own words. "I don't know; here is how I would find out" is a good answer. | **3.** Answers one question, or answers by reading from the screen. | **0.** Cannot answer. |

---

## E. AI disclosure and `prompts.md` (5 points)

| Row | Meets | Partly | Not yet |
|---|---|---|---|
| **E1. Disclosure and prompts** (5) | **5.** `AI-DISCLOSURE.md` is complete: tools, the rung, and one table row for each file or feature AI helped with (what you asked, kept, changed and rejected). `prompts.md` holds every prompt, in order, with dates, and it matches the disclosure. If you used no AI, the disclosure says so and `prompts.md` says "No prompts." | **2 to 3.** One of the two is incomplete, or they do not match. | **0.** Missing. |

Disclosed AI use within the rules never costs points anywhere in this rubric. AI use on the blueprint or the story text, or hidden AI use, is an academic-integrity matter, not a rubric row.

---

## Extra credit: stretch effects (up to +3)

| Meets (+3) | Partly (+1) |
|---|---|
| Effects in `display_ansi.py` or a layout in `display_curses.py`, **in addition to** your build feature, tuned to your story. Effects turn off when output is not a terminal, and `run_tests.py` still passes. | It works in a terminal, but piped output is not plain, or it breaks a test. |

If your build feature is (d) or (e), the effects are your feature, not extra credit. Extra credit cannot replace a missing row. **Instructor confirms** whether extra credit may raise a total above 100.

---

## Grader's quick sheet

| Row | Pts | Score | Note |
|---|---|---|---|
| A1 User stories, Given/When/Then, checks | 12 | | |
| A2 Map matches story.json | 8 | | |
| A3 Checker passes at the gate | 10 | | |
| A4 Cut list and lever | 5 | | |
| B1 Feature works, frozen files untouched | 10 | | |
| B2 Readable code | 5 | | |
| C1 Golden runs | 8 | | |
| C2 Peer playtest | 4 | | |
| C3 run_tests passes | 3 | | |
| D1 Plays live | 8 | | |
| D2 Map and one user story with its check | 8 | | |
| D3 One line of the feature | 8 | | |
| D4 Questions | 6 | | |
| E1 Disclosure and prompts | 5 | | |
| Extra credit | +3 | | |
| **Total** | **100** | | |
