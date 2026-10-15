# Lesson Sheets

One PRIMM sheet per lab, for the CYOA unit in CTI 110, Fall 2026. Dates, spine modules, PRIMM steps and rungs come from [`../UNIT-PLAN.md`](../UNIT-PLAN.md). If a sheet and the plan disagree, the plan wins.

**PRIMM** is Predict, Run, Investigate, Modify, Make. Students predict **before** they run. Each sheet hides its answers in a fold, so a student can check after.

**The AI Ladder rung** for each lab is in a box at the top of each sheet. The wording comes from `cti110-refresh-planning/CTI-110-ai-assistance-ladder.md`. The tutor setup and the one-command rung swap are in [`../ai-tutor/README.md`](../ai-tutor/README.md).

---

## The sheets

| Sheet | Date | Spine | PRIMM step | Rung | Demo file(s) in `course-cti110-26fa` |
|---|---|---|---|---|---|
| [P5LAB1-def-call-main.md](P5LAB1-def-call-main.md) | Tue 10/20/26 | M6 | Predict, Run, Investigate | 2 | `p5/p5lab1_before_norris.py`, `p5/p5lab1_norris.py` |
| [P5LAB2-parameters-return.md](P5LAB2-parameters-return.md) | Thu 10/22/26 | M6 | Investigate, Modify | 2 | `p5/p5lab2_trap_norris.py`, `p5/p5lab2_norris.py` |
| [P5LAB3-refactor.md](P5LAB3-refactor.md) | Tue 10/27/26 | M6 | Modify, Make | 3 | `p5/p5lab3_norris.py`, `p5/p5lab3_input.txt`, `p3lab_norris.py` |
| [P6LAB1-tutor-setup.md](P6LAB1-tutor-setup.md) | Tue 11/03/26 | P6 (the existing AI-tools module; not a spine module) | - | 2 (installed) | `p6/p6lab1_tutor_check.py`; config from `ai-tutor/rung-2/` |
| [P6LAB2-rooms-as-data-warmup.md](P6LAB2-rooms-as-data-warmup.md) | Thu 11/05/26 | M7 preview | Predict, Run, Investigate | 2 | `p6/p6lab2_rooms_norris.py` |
| [P7LAB1-dispatch-loop.md](P7LAB1-dispatch-loop.md) | Tue 11/10/26 | M7 | Investigate, Modify | 3 (swap the tutor) | `p7/p7lab1_norris.py` |
| [P7LAB2-load-a-story.md](P7LAB2-load-a-story.md) | Thu 11/12/26 | M7 | Predict, Run, Investigate, Modify | 3 | `p7/p7lab2_norris.py`, `p7/toy_story.json`; `cyoa_kit/` |
| [P7LAB3-save-file.md](P7LAB3-save-file.md) | Tue 11/17/26 | M7 | Modify, Make | 3 | `p7/p7lab3_norris.py`; `cyoa_kit/` (`s` and `l`) |
| [P7BONUS-sqlite.md](P7BONUS-sqlite.md) | Tue 11/17/26 (optional) | M7 | Modify, Make | 3 | `p7/p7bonus_sqlite_norris.py` |
| [FINAL1-blueprint.md](FINAL1-blueprint.md) | Thu 11/19/26 | M8 | Make (design) | No AI on the blueprint | `cyoa_kit/stories/fort_blueprint.md`, `dead_drop_blueprint.md` |
| [FINAL2-build-with-ai.md](FINAL2-build-with-ai.md) | Tue 11/24/26 (gate), Tue 12/01/26 | M8 | Make | 4 | `cyoa_kit/`, `cyoa_kit/tests/` |
| [FINAL3-playtest-and-present.md](FINAL3-playtest-and-present.md) | Thu 12/03/26; presentations Tue 12/08/26 and Thu 12/10/26 | M8 | - | 4 | `cyoa_kit/display_ansi.py`, `display_curses.py` |

Other dates (no sheet): Thu 10/29/26, P5 exit ticket and the midterm. Tue 12/15/26, the final exam. Instructor confirms both.

---

## What every sheet has

| Part | What it does |
|---|---|
| Title, date, spine module, PRIMM focus | Where the lab sits in the plan. |
| **AI today** box | The rung: what you may and may not do with AI today, in the Ladder's words. |
| Goal | One sentence. |
| Demo files | Paths in `course-cti110-26fa`. |
| Words for today | A short table of new words. |
| Predict, Run, Investigate, Modify, Make | Numbered questions. Predict comes **before** running. Answers are in folds. |
| Common mistakes | Mistake, what you see, fix. |
| Turn in | A checklist. |
| Exit check | Two or three questions. |

## The thread through the labs

| Lab | Hands on | Used later in |
|---|---|---|
| P5LAB1 | Name a block with `def`; start from `main()` | Every lab |
| P5LAB2 | A room **returns** the next room id; one loop moves the player | P7LAB1; the kit's `game.py` |
| P5LAB3 | Same input, same output, proved with `diff` | Golden runs in the final |
| P6LAB2 | Rooms as a dict of dicts | P7LAB1, P7LAB2 |
| P7LAB1 | A character sheet as a dict; the lever as a field (`role`) | `fields.role` in `story.json` |
| P7LAB2 | `json.load` a story; the checker | The blueprint gate |
| P7LAB3 | Save and load with JSON; flags as a sorted list | The kit's `s` and `l` keys |

## Fort text in the demos

The Fort rooms in the P5 to P7 demos (the docks, S1 to S3, C1 and C2) use sentences from the Fort on the Lake repository's own classroom files, `classroom/python/stage2` to `stage6`, sometimes shortened. A few plain lines that carry a game rule (for example, the Wizard oiling the cellar door in P7LAB1) are new. Nothing comes from any published module.
