# Unit Plan: Functions to Final Project (CYOA)

CTI 110, Fall 2026. Tuesday and Thursday. This plan starts Tue 10/20/26 and runs to the end of term in mid-December.

**Numbering: instructor confirms.** The labs continue the 26fa numbering. P4 (loops) ended with P4LAB2 on 10/8/26.

| 26fa module | What | Spine module | AI Ladder rung |
|---|---|---|---|
| P5 | Functions: 3 labs | M6 Functions | Rung 2 for P5LAB1 and P5LAB2; Rung 3 from P5LAB3 |
| P6 | The course's **existing** AI-tools module. We add only P6LAB1 (AI tutor setup) and P6LAB2 (a short rooms-as-data warm-up). We do not rewrite the module. | Not a spine module; it carries the M0 AI framing and the Ladder | Rung 2 tutor installed (AI as explainer) |
| P7 | Data refresher and files: 3 labs and an optional bonus | M7 Structured Data | Rung 3 (AI as reviewer) |
| Final | The CYOA final project | M8 Programming Miniproject | Blueprint: no AI. Build: Rung 4 (AI as collaborator) |

Why P5LAB1 and P5LAB2 stay at Rung 2 when the Ladder puts M6 at Rung 3: these are the first two days of a new idea, `def` and `return`. The Ladder's own reason for Rung 2 applies ("submitting generated code while learning syntax is lifting with a forklift"). Rung 3 begins in P5LAB3, where review fits the work: a refactor that already runs. The instructor can move Rung 3 earlier with no other change.

---

## 1. The arc in one line

Functions (rooms are functions that **return** the next room) → data (rooms and a character sheet as dicts) → files (a story loads from `story.json`; a character saves to a file) → the final project (user stories, a Mermaid map and `story.json` **first**; then a build with AI on the provided console engine; the checker verifies the story; the student presents).

Two worked examples run on the same engine through the whole unit:

| Story | File | The lever (field `role`) |
|---|---|---|
| *Fort on the Lake*: the Drowned Tower's island and first cellars | `cyoa_kit/stories/fort.json` | `fighter` or `wizard` (might or magic) |
| *High Tech, Low Lives*: *The Dead Drop*, cut down | `cyoa_kit/stories/dead_drop.json` | `enforcer` or `hacker` (chrome and muscle, or code) |

The lever is the same idea in both: an early choice about who the hero is, stored as a field, that later scenes test. Students build their own lever in the final.

---

## 2. Calendar

All demo files are in `course-cti110-26fa`. All lesson sheets are in `course-cti110-storming/cyoa-unit/lessons/`.

| Date | Session | Spine | PRIMM step | Rung | Demo file(s) | Lesson sheet |
|---|---|---|---|---|---|---|
| Tue 10/20/26 | **P5LAB1** Functions 1: `def`, call, `main()` | M6 | Predict, Run, Investigate | 2 | `p5/p5lab1_before_norris.py`, `p5/p5lab1_norris.py` | `P5LAB1-def-call-main.md` |
| Thu 10/22/26 | **P5LAB2** Functions 2: parameters and `return`; rooms return the next room id | M6 | Investigate, Modify | 2 | `p5/p5lab2_trap_norris.py`, `p5/p5lab2_norris.py` | `P5LAB2-parameters-return.md` |
| Tue 10/27/26 | **P5LAB3** Functions 3: refactor an earlier lab; identical output | M6 | Modify, Make | 3 | `p5/p5lab3_norris.py`, `p5/p5lab3_input.txt` (refactor of `p3lab_norris.py`) | `P5LAB3-refactor.md` |
| Thu 10/29/26 | P5 exit ticket, then the **midterm** (M0 to M6). Instructor confirms the date. | - | - | - | - | - |
| Tue 11/03/26 | P6 day 1: the existing AI-tools module, then **P6LAB1** AI tutor setup (about 40 minutes) | P6 | - | 2 installed | `p6/p6lab1_tutor_check.py`; config from `cyoa-unit/ai-tutor/rung-2/` | `P6LAB1-tutor-setup.md` |
| Thu 11/05/26 | P6 day 2: the existing module, then **P6LAB2** warm-up: rooms as data, AI as explainer (about 30 minutes) | M7 preview | Predict, Run, Investigate | 2 | `p6/p6lab2_rooms_norris.py` | `P6LAB2-rooms-as-data-warmup.md` |
| Tue 11/10/26 | **P7LAB1** Data refresher: rooms and a character sheet as dicts; the dispatch loop `room = ROOMS[room](hero)` | M7 | Investigate, Modify | 3 (swap tutor) | `p7/p7lab1_norris.py` | `P7LAB1-dispatch-loop.md` |
| Thu 11/12/26 | **P7LAB2** Files 1: `json.load` a story; first look at the kit | M7 | Predict, Run, Investigate, Modify | 3 | `p7/p7lab2_norris.py`, `p7/toy_story.json`; `cyoa_kit/` | `P7LAB2-load-a-story.md` |
| Tue 11/17/26 | **P7LAB3** Files 2: save and load a character; P7 exit ticket. Optional **P7BONUS** sqlite3. | M7 | Modify, Make | 3 | `p7/p7lab3_norris.py`; `p7/p7bonus_sqlite_norris.py` | `P7LAB3-save-file.md`; `P7BONUS-sqlite.md` |
| Thu 11/19/26 | **Final launch.** Deck *Sand Castle or Blueprint* (15 min). Exhibit 0. Blueprint workshop. | M8 | Make (design) | No AI on the blueprint | `cyoa_kit/stories/fort_blueprint.md`, `dead_drop_blueprint.md` | `FINAL1-blueprint.md` |
| Tue 11/24/26 | **Blueprint gate.** Blueprint and `story.json` due at the start of class. The checker must say `RESULT: PASS`. Instructor signs off, then the tutor swaps to Rung 4 and the build starts. | M8 | Make | 4 | `cyoa_kit/` | `FINAL2-build-with-ai.md` |
| Thu 11/26/26 | Thanksgiving. No class. | | | | | |
| Tue 12/01/26 | Build day: the build feature; record golden runs | M8 | Make | 4 | `cyoa_kit/tests/` | `FINAL2-build-with-ai.md` |
| Thu 12/03/26 | Peer playtest (Definition of Done); rehearse; optional stretch effects | M8 | - | 4 | `cyoa_kit/display_ansi.py`, `display_curses.py` | `FINAL3-playtest-and-present.md` |
| Tue 12/08/26 | **Presentations**, day 1 | M8 | - | - | - | `FINAL3-playtest-and-present.md` |
| Thu 12/10/26 | **Presentations**, day 2. Final packet due 11:59 pm. | M8 | - | - | - | - |
| Tue 12/15/26 | **Final exam** (exam week). Instructor confirms the date and time. | - | - | - | - | - |
| Thu 12/17/26 | Reserve: make-up presentations | | | | | |

**Slack.** If the existing AI-tools module needs more than two days, P6LAB2 moves to Tue 11/10 and P7LAB1 and P7LAB2 merge on Thu 11/12. The final dates do not move. The blueprint gate on 11/24 is the date to protect.

**Exit tickets.** The spine gates each module with a low-stakes exit ticket. P5's runs Thu 10/29 before the midterm. P6's belongs to the existing module. P7's runs Tue 11/17.

---

## 3. Lab by lab

### P5LAB1: def, call, main() (Tue 10/20)

**Goal.** A student can write a function with no parameters, call it, and start a program from `main()` at the bottom of the file.

**Bridge.** P4LAB2's `while again == "yes"` loop is the last thing they wrote. The "before" file is a short Fort walk that pastes the same banner and the same "check your torch" block three times. The "after" file names each block with `def` and calls it.

| Step | What students do |
|---|---|
| Predict | Read `p5lab1_before_norris.py`. How many times does the torch block run? Write the output for one walk. |
| Run | Run it. Compare. |
| Investigate | Read `p5lab1_norris.py`. Find each `def` and each call. Why is `main()` the last line? What happens if you move it to the top? (NameError: the function does not exist yet.) |

**Turn in.** `p5lab1_<lastname>.py`: three named functions and a `main()`, called at the bottom.

**Common mistakes** (from the Fort classroom's stage 3 and 4 tables, Python rows only): calling without parentheses (`if check:` is always true); `main()` at the top of the file; a function that prints when the caller needed the value.

### P5LAB2: parameters and return; rooms that return the next room (Thu 10/22)

**Goal.** A student can pass a value in, hand a value back with `return`, and use the result.

**The recursion trap.** M3BONUS made each door a function. That is good. The trap comes next: when a room function calls the next room function directly. `jetty()` calls `tower()`, and `tower()` calls `jetty()` to "go back". Each move starts a new call **inside** the old one, and the old one never finishes. Walk back and forth and the calls pile up. Python stops at about 1,000 calls deep with `RecursionError: maximum recursion depth exceeded`. Before that, any line written after a room call runs later, in reverse order, when the calls unwind, and prints things the player did not expect.

`p5lab2_trap_norris.py` shows it. Each room prints how deep the calls are. Typing `auto` walks back and forth until Python stops it, and the class reads the traceback together (a planned error, as the spine asks).

**The fix.** A room never calls a room. A room **returns the id of the next room**, as a string. One loop in `main()` moves the player:

```python
room = "jetty"
while room != "end":
    if room == "jetty":
        room = jetty(hero_name)
    elif room == "tower":
        room = tower(hero_name)
```

The calls never pile up: each room finishes before the next one starts. This is the shape of the kit's engine, and of every game loop the students will meet.

| Step | What students do |
|---|---|
| Investigate | In the trap file, find the line that calls a room from inside a room. In the fixed file, find where the next room comes from. |
| Modify | Add a parameter: pass the hero's name in and print it. Add a room `cottage` that returns `"tower"`. |

**Turn in.** `p5lab2_<lastname>.py`: at least three rooms, each with one parameter, each returning the next room id; one `while` loop in `main()`.

**Common mistakes.** Forgetting `return` (the room returns `None` and the loop runs forever or stops with an error); calling a room and not saving its result (`jetty(name)` instead of `room = jetty(name)`); argument order.

### P5LAB3: refactor with identical output (Tue 10/27)

**Goal.** Code is revised, not just written. A student turns a working lab into functions and **proves** the output did not change.

**Demo.** `p3lab_norris.py` (making change) pastes the same coin block five times. `p5/p5lab3_norris.py` turns it into `count_coins(cents, size)`, which returns two values (how many coins, cents left), and `show_count(count, singular, plural)`. The proof:

```
python3 p3lab_norris.py < p5/p5lab3_input.txt > before.txt
python3 p5/p5lab3_norris.py < p5/p5lab3_input.txt > after.txt
diff before.txt after.txt
```

No output from `diff` means the same output. This is the golden-run idea the final project uses.

| Step | What students do |
|---|---|
| Modify | Refactor their own P3LAB or P4LAB2 into functions. |
| Make | Prove identical output with an input file and `diff`. |
| Review (Rung 3) | Only after it works and matches: ask an AI to review it. Write a two-line note: what you changed because of the review, and why. Or what you did not change, and why. |

**Turn in.** `p5lab3_<lastname>.py`, the input file, and the review note as a comment block at the top.

### P6LAB1: AI tutor setup (Tue 11/03, inside the existing module)

**Goal.** Each student's Codespace has a tutor that teaches instead of answering. It acts like Claude Code's Learning style: it asks the student to write the key lines, explains why, gives hints before answers, checks understanding, and never hands over a whole solution above the student's rung.

Students copy one folder (`ai-tutor/rung-2/`) into the root of their repository with one command. It covers GitHub Copilot (`.github/copilot-instructions.md`), Claude Code (`CLAUDE.md`, `.claude/settings.json`, `.claude/output-styles/cti110-tutor.md`) and any other tool that reads `AGENTS.md`.

**Check that it works.** `p6/p6lab1_tutor_check.py` has a small, planted bug. The student asks the tutor about it. A working tutor asks a question or gives a hint first, and does not paste the fixed program. The student fills a short checklist on the lesson sheet.

This lab also shows how to turn off Copilot's inline suggestions, as the Ladder asks.

### P6LAB2: warm-up, rooms as data (Thu 11/05, inside the existing module)

**Goal.** First sight of rooms as data, with the tutor as explainer.

`p6/p6lab2_rooms_norris.py` holds three Fort rooms as a dict of dicts (`title`, `text`, `exits`). One loop shows a room and follows an exit. Students predict the output, run it, and ask the tutor to explain two lines they do not understand. They write the tutor's explanation in their own words. No Modify or Make today; P7 does that.

### P7LAB1: data refresher and the dispatch loop (Tue 11/10)

**Goal.** Lists and dicts again (students met them in P2: `p2lab2_norris.py` and `p2hw2_setup.py`), now holding a game.

Start of class: swap the tutor to Rung 3 (one command).

`p7/p7lab1_norris.py` keeps P5LAB2's room functions and replaces the `if`/`elif` chain with a dict of functions:

```python
ROOMS = {
    "jetty": jetty,
    "tower": tower,
    "cottage": cottage,
}
room = "jetty"
while room != "end":
    room = ROOMS[room](hero)
```

`hero` is a character sheet dict: `name`, `role` (`"fighter"` or `"wizard"`), `hp`, and `items` (a list). The lever appears: the tower's door checks `hero["role"]`.

| Step | What students do |
|---|---|
| Investigate | What is `ROOMS["tower"]`? What does `ROOMS["tower"](hero)` do? Why no parentheses inside the dict? |
| Modify | Add a room. Add an item to `hero["items"]` in one room and test for it in another. |

**Turn in.** `p7lab1_<lastname>.py`, then the Rung 3 review note.

### P7LAB2: files 1, load a story (Thu 11/12)

**Goal.** The story leaves the Python. It becomes data in a file.

`p7/toy_story.json` is the tiny example from `final-project/STORY-FORMAT.md`, section 9. `p7/p7lab2_norris.py` opens it with `json.load`, prints the title, and walks the scenes with a short loop: show the beats, number the options, follow `to`, `next` or `ending`. It ignores `when` on purpose.

| Step | What students do |
|---|---|
| Predict | Read `toy_story.json`. Write the screens you will see if you pick 1, then 1. |
| Run | Run the demo. Then run the kit on the same file: `python3 game.py stories/toy.json`. What does the kit do that the demo does not? (It hides options by `when`.) |
| Investigate | Find, in the kit's `engine.py`, the function that hides options. |
| Modify | Add a third ending to `toy_story.json`. Run the checker: `python3 checker.py stories/toy.json`. Break the file on purpose (misspell a `to`) and read what the checker says. |

**Turn in.** The changed story and one paragraph: what the checker said about the broken file.

### P7LAB3: files 2, save and load a character (Tue 11/17)

**Goal.** A program can stop and start again where it left off.

`p7/p7lab3_norris.py` builds a character sheet dict, saves it with `json.dump`, loads it with `json.load`, and checks that the two are equal. It shows the trap: a Python `set` cannot be saved as JSON (`TypeError: Object of type set is not JSON serializable`). That is why the kit keeps flags as a **sorted list**.

Then, in the kit: play the Fort story, press `s`, quit, start again, press `l`. Open `save_fort.json` and read the state.

**Turn in.** `p7lab3_<lastname>.py`, which saves and loads a character with at least one list in it.

**P7BONUS (optional): sqlite3.** The spine's M7 ends with sqlite3 as the "database fundamentals" line of the CCL. `p7/p7bonus_sqlite_norris.py` stores each ending a player reaches in a sqlite3 table and prints "Endings found: 2 of 3". The instructor decides whether this is a bonus or required (see section 5).

### Final project (Thu 11/19 to Thu 12/10)

The full packet is in `final-project/`: `ASSIGNMENT.md`, `RUBRIC.md`, `AI-DISCLOSURE.md`, `STRETCH-EFFECTS.md`, `STORY-FORMAT.md`, `BLUEPRINT-TEMPLATE.md`, `EXHIBIT-0.md`.

| Phase | Dates | Student does | AI |
|---|---|---|---|
| Launch | Thu 11/19 | Watch the deck. Do Exhibit 0: find what a naive prompt chain leaves out (who plays it, how you know it works, a limit, what you leave out). Start the blueprint. | None on the blueprint (formulation is graded as theirs) |
| Blueprint gate | Tue 11/24 | Hand in `stories/blueprint.md` (3 to 6 user stories, each with a Given/When/Then and how it is checked; a Mermaid map; a cut list; the lever) and `stories/story.json`. The checker must pass. | None |
| Build | Tue 11/24 to Thu 12/03 | One build feature from the menu, in `game.py`, a display module or a new file. Golden runs: one `tests/story_<ending>.in` for each ending claimed. Save every prompt in `prompts.md`. | Rung 4 tutor: collaborator on code, never on `engine.py`, `checker.py`, the story text or the blueprint |
| Done | Thu 12/03 | Definition of Done: the checker passes; `run_tests.py` passes; every user story has a check; a classmate played it and signed the playtest form. | |
| Present | Tue 12/08, Thu 12/10 | 5 minutes: play one golden run live, show the map and one user story with its check, explain one line of the build feature, answer questions. A student who cannot explain their own software fails the presentation. | |

---

## 4. What each lab hands to the next

| From | Hands on | Used in |
|---|---|---|
| P5LAB2 | Rooms return the next room id; one loop moves the player | P7LAB1 dispatch loop; the kit's `game.py` |
| P5LAB3 | Same input, same output, prove it with `diff` | Golden runs and `run_tests.py` |
| P6LAB1 | The tutor, and the one-command rung swap | P7 (Rung 3) and the final (Rung 4) |
| P7LAB1 | A character sheet as a dict; the lever as a field | `fields.role` in `story.json` |
| P7LAB2 | `json.load` a story; the checker | The blueprint gate |
| P7LAB3 | Save and load with JSON; flags as a sorted list | The kit's `s` and `l` keys |

---

## 5. Decisions for the instructor

1. **Numbering.** P5, P6, P7 and the final as above. Confirm.
2. **Midterm and final exam dates.** Placed on Thu 10/29 and Tue 12/15. Confirm.
3. **Rung 2 for P5LAB1 and P5LAB2.** Can move to Rung 3 with no other change.
4. **sqlite3.** The spine's M7 includes a sqlite3 recap, which is the course's "database fundamentals" line in the CCL crosswalk. This unit keeps it as P7BONUS. Make it required if the crosswalk needs it.
5. **Spec-first gate before M8.** The spine's open question 2 asks for a small spec-first gate in M5 or M7. P7LAB2's "add a third ending, then run the checker" is a candidate. A one-line user story could be added to it.
