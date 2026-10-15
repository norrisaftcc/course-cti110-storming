# The CYOA Unit

CTI 110, Fall 2026. Functions, data and files, built toward one final project: a choose-your-own-adventure game that runs in the console.

The student writes the **blueprint first**: user stories, a Mermaid map, and the story itself as `story.json`. Then they build on a provided engine, with AI as a collaborator. A checker proves the story works. The student presents it live.

The unit's claim, taken from the *Neon Wake* module: a quick prototype is fine. The failure is turning a prototype into a product without a design pass. A student who writes the blueprint first knows what to ask the AI for, and can tell when the answer is wrong.

---

## Use it

| You want to | Go to |
|---|---|
| See the plan, lab by lab and date by date | [`UNIT-PLAN.md`](UNIT-PLAN.md) |
| Know the story file format, the engine and the display functions | [`final-project/STORY-FORMAT.md`](final-project/STORY-FORMAT.md). This is the contract. |
| Teach a lab | [`lessons/`](lessons/): one PRIMM sheet per lab |
| Launch the final project | [`deck/sandcastle-or-blueprint.html`](deck/sandcastle-or-blueprint.html), then [`final-project/ASSIGNMENT.md`](final-project/ASSIGNMENT.md) |
| Grade the final | [`final-project/RUBRIC.md`](final-project/RUBRIC.md) |
| Set up the AI tutor in a Codespace | [`ai-tutor/README.md`](ai-tutor/README.md) |
| Play a worked example | In `course-cti110-26fa/cyoa_kit/`: `python3 game.py stories/fort.json` |
| Check a story | `python3 checker.py stories/fort.json` |
| Run every test | `python3 tests/run_tests.py` (expect `ALL TESTS PASSED`) |
| See where every borrowed idea came from | [`SOURCES.md`](SOURCES.md) |

Everything runs on Python 3.10 or newer with the standard library only. Nothing to install. The optional curses display needs `pip install windows-curses` on Windows only.

---

## Where things are

The unit lives in two repositories. Curriculum design is here. Code the class types or runs is in the 26fa repository.

### `course-cti110-storming/cyoa-unit/` (this folder: design and teaching)

| Path | What it is |
|---|---|
| `README.md` | This page. |
| `UNIT-PLAN.md` | The calendar from Tue 10/20/26 to the presentations; each lab mapped to the spine module, the PRIMM step and the AI Ladder rung. |
| `SOURCES.md` | Every borrowed source, with repository, path, commit and what we took. |
| `lessons/` | PRIMM sheets: `P5LAB1-def-call-main.md`, `P5LAB2-parameters-return.md`, `P5LAB3-refactor.md`, `P6LAB1-tutor-setup.md`, `P6LAB2-rooms-as-data-warmup.md`, `P7LAB1-dispatch-loop.md`, `P7LAB2-load-a-story.md`, `P7LAB3-save-file.md`, `P7BONUS-sqlite.md`, `FINAL1-blueprint.md`, `FINAL2-build-with-ai.md`, `FINAL3-playtest-and-present.md`, and an index, `README.md`. |
| `final-project/STORY-FORMAT.md` | The contract: story schema (a strict subset of the Stage script schema), state, conditions, the lever, dice, the engine API, the console, test vectors, the checker's rules, the display interface. |
| `final-project/ASSIGNMENT.md` | The student assignment. |
| `final-project/RUBRIC.md` | The rubric. |
| `final-project/AI-DISCLOSURE.md` | The disclosure template students fill. |
| `final-project/STRETCH-EFFECTS.md` | The optional stretch: ANSI or curses effects through a swappable display module. |
| `final-project/BLUEPRINT-TEMPLATE.md` | User stories, Given/When/Then, the Mermaid map, the cut list. |
| `final-project/EXHIBIT-0.md` | A naive prompt chain for a text adventure, and the four questions it never asks. |
| `deck/sandcastle-or-blueprint.html` | A 15-minute, single-file slide deck for the final-project launch. |
| `ai-tutor/` | Tutor configs for Codespaces, one folder per rung (`rung-2/`, `rung-3/`, `rung-4/`), and a student handout. |
| `instructor/scan_fort_names.py` | Scans the Fort example for the Fort repository's forbidden names. It reads the lists from the Fort repository at run time; it does not copy them. |

### `course-cti110-26fa/` (code typed in class, and the kit)

| Path | What it is |
|---|---|
| `p5/` | Functions demos: `p5lab1_before_norris.py`, `p5lab1_norris.py`, `p5lab2_trap_norris.py`, `p5lab2_norris.py`, `p5lab3_norris.py`, `p5lab3_input.txt` |
| `p6/` | `p6lab1_tutor_check.py` (a planted bug to test the tutor), `p6lab2_rooms_norris.py` |
| `p7/` | `p7lab1_norris.py`, `p7lab2_norris.py`, `toy_story.json`, `p7lab3_norris.py`, `p7bonus_sqlite_norris.py` |
| `cyoa_kit/README.md` | How to play, check and test; what a student may change. |
| `cyoa_kit/engine.py` | The rules. Pure functions, no classes, no printing. Frozen for students. |
| `cyoa_kit/game.py` | The console loop. Students may change it in the final. |
| `cyoa_kit/display_plain.py` | The default display: plain ASCII. The reference for all test output. |
| `cyoa_kit/display_ansi.py` | Colour, typewriter, boxes, meter bars. Turns itself off when output is not a terminal or `NO_COLOR` is set. |
| `cyoa_kit/display_curses.py` | A full-screen display with `curses`. |
| `cyoa_kit/checker.py` | Checks a story: shape, every path, every ending, the lever. |
| `cyoa_kit/stories/` | `toy.json`, `fort.json`, `dead_drop.json`, and the two worked blueprints `fort_blueprint.md`, `dead_drop_blueprint.md`. |
| `cyoa_kit/tests/` | `run_tests.py`, golden runs (`.in` and `.out`), engine checks, and stories broken on purpose in `tests/broken/`. |

---

## How the unit runs

1. **P5, functions.** Rooms become functions. Then the trap: a room that calls a room piles up calls until Python stops it. The fix is the shape of every game loop: a room **returns** the next room's id, and one loop moves the player.
2. **P6, the existing AI-tools module.** We add the tutor setup and a 30-minute warm-up. The tutor is installed at Rung 2 (explainer).
3. **P7, data and files.** Rooms in a dict; the character sheet as a dict; then the story moves out of Python into `story.json`. A character saves to a file and loads back. The tutor moves to Rung 3 (reviewer).
4. **The final.** Blueprint first, checked by the checker, signed off. Then the tutor moves to Rung 4 (collaborator) and the student builds one feature on the kit, records golden runs, gets a classmate to play it, and presents.

---

## Read this before you rely on it

- **The worked examples and the kit were built with AI**, from the sources in `SOURCES.md`. A person must play both stories to every ending, read every line of `engine.py`, and run `run_tests.py` before the unit is used with students.
- **The Fort example follows the Fort repository's rules.** Its text comes from the Fort repository's own classroom material and Module 2, not from any published module. It stays on the island and in the first cellars. Run `instructor/scan_fort_names.py` after any change to it.
- **The Dead Drop example is a cut.** The lever (Enforcer or Hacker), the pass options that test it, and the cover group are new for this unit, not part of the original Twine. Its blueprint labels them that way.
- **The AI tutor is guidance, not a lock.** Instruction files steer a tool; they do not stop a student from asking it to do more. The Ladder's enforcement is the assignment design: the blueprint gate, the golden runs and the presentation. The tutor makes the right use easy.
- **The Stage claim is "every key is a Stage key".** A story file is not a drop-in Stage pack. `STORY-FORMAT.md` section 13 lists what a converter would add.
