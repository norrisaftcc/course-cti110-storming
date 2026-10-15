# Final Project: Your Own Adventure

CTI 110, Fall 2026 · Spine module M8, Programming Miniproject · AI Ladder: no AI on the blueprint; Rung 4 for the build

---

## The idea: blueprint first, then build

You will make a choose-your-own-adventure game that runs in the console. You write the design first: who plays it, how you will know it works, and what you leave out. Then you build on a game engine we give you, with an AI assistant as your collaborator. A checker proves your story works. Then you stand up and show it. A quick test build is fine, as long as you know that is what it is. A spike that answers a question and is then thrown away is good practice. The failure is a spike that is promoted without a design pass.

We grade most heavily the two things AI cannot do for you: **knowing what to build**, and **standing behind what you built**.

---

## 1. Timeline

| Date | What happens | What is due |
|---|---|---|
| Thu 11/19/26 | **Launch.** The deck *Sand Castle or Blueprint*. Exhibit 0. Start your blueprint in class. | Nothing. Start. |
| Tue 11/24/26 | **Blueprint gate.** | `stories/blueprint.md` and `stories/story.json`, **at the start of class**. `python3 checker.py stories/story.json` must print `RESULT: PASS`. The instructor signs off. Then the build starts. |
| Tue 11/24 to Thu 12/3/26 | **Build.** One build feature. Golden runs. (Thu 11/26 is Thanksgiving: no class.) | Work in progress. Build day in class Tue 12/1. |
| Thu 12/3/26 | **Playtest.** A classmate plays your game and signs your form. Rehearse your talk. | The signed playtest form. |
| Tue 12/8/26 and Thu 12/10/26 | **Presentations.** The instructor posts the order. | Your 5-minute presentation. |
| Thu 12/10/26, 11:59 pm | **Packet due.** | Everything in section 9, pushed to GitHub. |

---

## 2. Set up

1. Copy the whole `cyoa_kit` folder from the class repository into your own repository.
2. Open a terminal **inside** `cyoa_kit`. Run these three commands. They should work before you change anything:

   ```
   python3 game.py stories/fort.json
   python3 checker.py stories/fort.json
   python3 tests/run_tests.py
   ```

   The last line of the third command must be `ALL TESTS PASSED`.
3. Make your files. All paths are inside `cyoa_kit/`:

| Your file | What it is |
|---|---|
| `stories/story.json` | Your story. Every word of your game and every rule of its world. The format is in `STORY-FORMAT.md`, sections 1 to 8. |
| `stories/blueprint.md` | Your design. Copy `BLUEPRINT-TEMPLATE.md` and fill it in. |
| `tests/story_<ending id>.in` and `tests/story_<ending id>.out` | Golden runs: one pair for each ending you claim, **at least 3**. Example: `tests/story_escaped.in`. |
| `prompts.md` | Every prompt you sent to an AI, in order, with the date. Save your prompts; the prompt is half the artifact. |
| `AI-DISCLOSURE.md` | Copy `AI-DISCLOSURE.md` from this folder and fill it in. |

Do not delete the worked examples (`fort.json`, `dead_drop.json`, `toy.json`) and their tests. They prove the engine still works.

Give your story an `id` of your own, such as `"lighthouse"`. Do not use `toy`, `fort` or `dead_drop`.

---

## 3. Your story: what it must have

| Must have | Means | How it is checked |
|---|---|---|
| 6 to 15 scenes | Not counting endings. | Checker rule 20. It is only a **warning** in the checker, but for this project a rule 20 warning counts as a miss. |
| At least 3 endings | Every ending can be reached. | Checker rules 15 and 20 |
| A lever named `role` | A field named `role`, set by an option in the **start** scene. Each value opens at least one option that the other values never see. Each value can reach an ending. | Checker rule 18 |
| A flag that opens a choice | An effect sets a flag. Later, an option with `"when": { "flag": ... }` shows only because of it. | You show it: in your map (an edge labelled `(flag ...)`) and in the State table of your blueprint. The checker only checks that the flag is set somewhere (rule 10). |
| A real decision | At least one choice that changes **which endings can still happen**. Two options that lead to the same endings are not a decision. | Checker rule 17 |
| No stuck spots | From anywhere the player can be, some ending can still be reached. | Checker rule 16 |

The checker's last line must be exactly:

```
RESULT: PASS (0 problems, N warnings)
```

Read every warning. You must be able to say why each one is there. If the checker says `engine.py has changed since the kit was made`, put the kit's `engine.py` back.

---

## 4. The build: pick ONE feature

| | Feature | Done means |
|---|---|---|
| (a) | **An endings-found tracker.** Each ending the player reaches is saved to `endings_found_<id>.json`. The title screen shows `Endings found: 2 of 4`. | Reach an ending, restart, and the count goes up. The same ending twice counts once. |
| (b) | **A character sheet key.** Typing `c` at a choice prints the hero's fields, meters and flags. | `c` works at any choice and changes nothing in the game. |
| (c) | **A story-so-far log.** Each scene and each pick is written to a text file, such as `log_<id>.txt`. | After one play, the file reads like a short retelling. |
| (d) | **Effects tuned to your story.** Colours, typewriter speed, meter bars or boxes in `display_ansi.py`. See `STRETCH-EFFECTS.md`. | It looks different in a terminal. Piped output is still plain. |
| (e) | **A curses layout.** A full-screen layout in `display_curses.py`. See `STRETCH-EFFECTS.md`. | It runs in a terminal and puts the terminal back when you quit. |
| (f) | **Your own idea.** Ask the instructor first, by Tue 12/1. | You and the instructor agree on it in writing. |

**Write the feature's user story first.** Before you ask an AI for any code, add one user story for your feature to `blueprint.md` (call it US-F), with Given/When/Then and a check. Write it yourself.

**Rules for the build:**

| Rule | Why |
|---|---|
| Your feature lives in `game.py`, a `display_*.py` file, or a new `.py` file. | These are the files you own. |
| **Never edit `engine.py`, `checker.py` or `tests/run_tests.py`.** | They are frozen. The checker warns if `engine.py` changes. The story lives in `story.json`, not in the Python. |
| No `class` and no `global`. | The course does not teach them. `run_tests.py` checks every `.py` file in the kit. |
| Every `.py` file you write or change starts with the class header (CTI 110, the lab name, your name, the date). | The same as every lab this term. |
| After a deliberate change to the output, run `python3 tests/run_tests.py --regen`, then read the diff (`git diff tests/`; commit first, so the diff shows only the new change). | `--regen` rewrites every `.out` file. Only you can say whether each change was meant. |

---

## 5. Definition of Done

Your project is done when all four lines are true:

- [ ] The checker prints `RESULT: PASS`.
- [ ] `python3 tests/run_tests.py` prints `ALL TESTS PASSED`.
- [ ] Every user story has a criterion and a check.
- [ ] A classmate played it and signed the playtest form.

---

## 6. What AI may and may not do

The Ladder says: you may use AI exactly to the degree that you can check its output.

| Phase | Dates | AI | You may | You may not |
|---|---|---|---|---|
| **Blueprint** | Thu 11/19 to Tue 11/24 | **None** | Ask the instructor, a tutor or a classmate. Read the checker's messages. | Use AI on `blueprint.md` or `story.json`: not for ideas, not for user stories, not for the map, not for fixing the JSON. |
| **Build** | Tue 11/24 to Thu 12/3 | **Rung 4: AI as collaborator** | Ask AI to write, explain and review code for your feature. Ask it to explain an error, a checker line or a failing test. Ask it to help you find a bug. | Ask AI to edit `engine.py`, `checker.py` or `tests/run_tests.py`. Ask it to write or rewrite your **story text** (any title, beat, ask, label or sub in `story.json`) or your blueprint. Ask it to write `prompts.md` or `AI-DISCLOSURE.md`. Use code you cannot explain. |
| **Present** | Tue 12/8, Thu 12/10 | None | Use your own notes. | Read an AI's explanation aloud as your answer. |

**Set up your tutor for Rung 4 at the gate.** The tutor files are in `ai-tutor/rung-4/`, at the top of your class repository. The one-command swap is in `ai-tutor/README.md`. After the swap, ask your tutor "What rung are you on?" It should say Rung 4. At Rung 4 it still asks you to write the key lines and explain them back. That is on purpose: you have to present this code.

**Disclosure.** Disclosure is normal professional practice, not a confession. Fill in `AI-DISCLOSURE.md` and keep `prompts.md` as you go; AI help that is within these rules and disclosed never costs you points.

---

## 7. Golden runs

A golden run is a file of typed answers and the exact output they make. You need one for each ending you claim (at least 3).

1. Run `python3 checker.py stories/story.json`. Find a line like `OK shortest way to escaped (role keeper): type 1 2 1 1 (4 picks)`.
2. Make `tests/story_escaped.in`. The first line is the header. Then one answer per line, then `q`:

   ```
   # story: stories/story.json seed: 1
   # The keeper reaches the escaped ending.
   1
   2
   1
   1
   q
   ```

3. Run `python3 tests/run_tests.py --regen`. It writes `tests/story_escaped.out`.
4. **Read the `.out` file.** Does it end at the ending you meant? If not, fix the `.in` file and go back to step 3.
5. Run `python3 tests/run_tests.py`. It must print `ALL TESTS PASSED`.

If your story has a dice roll, the checker says which result a path needs, such as `(needs success)`. Try other seeds in the header until the roll gives that result.

The lesson sheet `lessons/FINAL2-build-with-ai.md` walks through this step by step.

---

## 8. The presentation

**5 minutes, then questions.** Bring your laptop or use the class machine. Run it from your repository.

| Part | About | What you do |
|---|---|---|
| Play it live | 1.5 min | Play one golden run in the terminal. Say what the lever is when you choose it. |
| The map and one user story | 1.5 min | Show your Mermaid map. Pick one user story. Read its Given/When/Then. Show its check passing. |
| One line of your feature | 1.5 min | Open your feature's code. Pick one line. Explain what it does and why it is there. |
| Wrap up | 0.5 min | One thing you cut, and why. |
| Questions | 2 to 3 min | The instructor and the class ask. |

**A student who cannot explain their own software fails the presentation.** This holds even if the game runs. It does not matter who typed the code. If it is in your project, you must be able to explain it.

---

## 9. Turn in (by Thu 12/10/26, 11:59 pm)

Push your repository to GitHub. Turn in its link.

- [ ] `cyoa_kit/stories/story.json` (the checker prints `RESULT: PASS`)
- [ ] `cyoa_kit/stories/blueprint.md` (all ten sections, plus US-F for your feature, plus any dated notes on changes after the gate)
- [ ] `cyoa_kit/tests/story_<ending id>.in` and `.out`, at least 3 pairs
- [ ] Your feature, in `game.py`, a `display_*.py` file or a new `.py` file
- [ ] `cyoa_kit/prompts.md`
- [ ] `cyoa_kit/AI-DISCLOSURE.md`
- [ ] The signed playtest form (a photo or scan in the repository is fine)

**Changes after the gate.** You may change your story during the build. If you do, add a short dated note at the end of `blueprint.md`: what changed and why. Write it yourself. The blueprint is graded as you handed it in at the gate.

**Grading.** See `RUBRIC.md`. Blueprint 35, build 15, verification 15, presentation 30, AI disclosure 5. The blueprint and the presentation together are 65 of 100.

---

## Files in this folder

| File | What it is |
|---|---|
| `STORY-FORMAT.md` | The story file format and the checker's rules. Students read sections 1 to 8. |
| `BLUEPRINT-TEMPLATE.md` | Copy it to `stories/blueprint.md`. |
| `EXHIBIT-0.md` | The launch-day worksheet. |
| `RUBRIC.md` | How you are graded. |
| `AI-DISCLOSURE.md` | The disclosure template. |
| `STRETCH-EFFECTS.md` | Optional: colours and a full-screen layout. |

Worked examples, in `cyoa_kit/stories/`: `fort.json` with `fort_blueprint.md`, and `dead_drop.json` with `dead_drop_blueprint.md`.
