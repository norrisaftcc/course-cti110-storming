# FINAL2: Build with AI

**Dates:** Tue 11/24/26 (the blueprint gate, then the build starts) and Tue 12/1/26 (build day) · **Spine module:** M8 Programming Miniproject · **PRIMM focus:** Make

> **AI today: Rung 4. AI as collaborator.**
>
> | You may | You may not |
> |---|---|
> | Ask AI to write, explain and review code for your build feature, in `game.py`, a `display_*.py` file or a new `.py` file. | Ask AI to edit `engine.py`, `checker.py` or `tests/run_tests.py`. |
> | Ask AI to explain an error, a checker line or a failing test. | Ask AI to write or rewrite your story text or your blueprint. |
> | Ask AI to help you find a bug. | Use code you cannot explain. You present this code on 12/8 or 12/10. |
>
> The Ladder: "Full assistance permitted for implementation. Problem formulation, spec, and presentation are yours, and are graded heavily."

**Goal.** You build one feature on the kit with AI as a collaborator, and you prove your story works with golden runs. Every change you keep, you can explain.

**Files** (in your copy of `cyoa_kit/`):

| File | Who owns it today |
|---|---|
| `stories/story.json`, `stories/blueprint.md` | You. No AI. |
| `game.py`, `display_plain.py`, `display_ansi.py`, `display_curses.py`, a new `.py` file | You, with AI. |
| `engine.py`, `checker.py`, `tests/run_tests.py` | Frozen. Nobody edits them. |
| `tests/story_<ending id>.in` and `.out` | You write the `.in`. `--regen` writes the `.out`. |
| `prompts.md`, `AI-DISCLOSURE.md` | You, as you go. |

---

## Words for today

| Word | Means |
|---|---|
| **the gate** | The check at the start of class on 11/24: blueprint and `story.json` handed in, and the checker prints `RESULT: PASS`. |
| **Rung 4** | AI as collaborator. It may help write code. The design and the talk stay yours. |
| **frozen file** | A file you never change: `engine.py`, `checker.py`, `tests/run_tests.py`. |
| **golden run** | A file of typed answers (`.in`) and the exact output they make (`.out`). |
| **`--regen`** | Tells `run_tests.py` to rewrite every `.out` file from what the game prints now. |
| **US-F** | The user story for your build feature. You write it before you ask for code. |

---

## 1. At the gate (Tue 11/24, first 15 minutes)

1. Run `python3 checker.py stories/story.json`. Show the instructor the last line: `RESULT: PASS (0 problems, N warnings)`.
2. The instructor signs off. Commit: `git add -A` then `git commit -m "Blueprint gate"`. This commit is your blueprint as graded.
3. Pick your build feature from `ASSIGNMENT.md` section 4.
4. Write **US-F** in `blueprint.md`, yourself: As a player, I want ..., so that .... Given/When/Then. Check.

## 2. Swap the tutor to Rung 4 (5 minutes)

Run the Rung 4 swap command from the root of your repository. The command is in `ai-tutor/README.md`. It copies the files from `ai-tutor/rung-4/` over your Rung 3 files.

Then ask your tutor:

1. "What rung are you on?" It should say Rung 4.
2. "Will you write story text for me?" It should say no, and tell you why.

If it gives a different answer, check that you ran the command from the root of your repository, then ask the instructor.

## 3. The build loop

Repeat these five steps for every change. Small changes. One at a time.

| Step | What you do | Why |
|---|---|---|
| 1. **Ask** | Paste your US-F and the part of the code you want to change. Ask for one small step, not the whole feature. | A small answer is one you can check. |
| 2. **Read** | Read the answer before you paste it. Find each new name. Where is it defined? Where is it used? | Code you have not read is code you cannot present. |
| 3. **Run** | Run the game. Then `python3 checker.py stories/story.json` and `python3 tests/run_tests.py`. | The checker must still pass. The tests tell you what the change broke. |
| 4. **Explain it back** | In your own words, out loud or in a comment: what does this change do, and why is it there? If you cannot, ask the tutor to explain, then try again. Or throw the change away. | This is your presentation, practised now. |
| 5. **Log it** | Paste the prompt into `prompts.md`, numbered and dated. Add a row to `AI-DISCLOSURE.md` when you keep, change or reject something. | Save your prompts; the prompt is half the artifact. |

A good first prompt, as an example:

> Here is my user story US-F: [paste it]. Here is `game.py`'s `handle_answer` function: [paste it]. I want to add the `c` key. What is the smallest change? Do not write the whole thing; show me where it goes and let me write the key line.

5. Your tutor asks you to write a line yourself. Why does it do that at Rung 4?

<details><summary>Answer</summary>

5. You will explain one line of your feature in the presentation. The tutor is set up to make you write and explain the key lines, so that you can. It still helps; it just does not hand over the whole thing.

</details>

## 4. Record your golden runs

You need one golden run for each ending you claim, at least 3. Do this for each ending.

1. Run the checker. Find the "shortest way" line for the ending:

   ```
   OK shortest way to escaped (role keeper): type 1 2 1 1 (4 picks)
   ```

2. Make the file `tests/story_escaped.in`. The ending id goes in the name. The first line is exactly the header below. Then one number per line, from the checker. Then `q`:

   ```
   # story: stories/story.json seed: 1
   # The keeper reaches the escaped ending by the shortest way.
   1
   2
   1
   1
   q
   ```

3. Write the `.out` file:

   ```
   python3 tests/run_tests.py --regen
   ```

   The first time, this also writes `tests/check_<your story id>.out`, the checker's report on your story.
4. **Read `tests/story_escaped.out`.** Scroll to the end. Does it say the ending's title, `THE END`, and a trail that ends with `escaped`? If not, your `.in` is wrong: fix it and go back to step 3.
5. Run the tests for real:

   ```
   python3 tests/run_tests.py
   ```

   The last line must be `ALL TESTS PASSED`.

6. Why does `run_tests.py` also run each `.in` with `--display ansi`?
7. You changed one line of story text after recording your runs. Now three tests fail. What do you do?

<details><summary>Answers</summary>

6. To prove the effects turn off when output is not a terminal. Piped ANSI output must be exactly the plain output.
7. Run `--regen`, then read the diff (`git diff tests/`). If the only changes are the line you meant to change, the change was deliberate: commit it. If anything else changed, find out why before you commit.

</details>

**A story with dice.** If the checker's line ends `(needs success)` or `(needs fail)`, the roll must go that way. Change the seed in the header (`seed: 2`, `seed: 3`, ...), run `--regen`, and read the `.out` until the roll gives that result.

**A feature that changes the output.** If your feature changes what the game prints (a new title-screen line, a new key in the help), every `.out` file changes, including the Fort and Dead Drop ones. That is expected. Commit first, run `--regen`, then read `git diff tests/`. Every change should be one you meant.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Asking for the whole feature in one prompt | A long answer you cannot explain. | Ask for one step. Then the next. |
| Letting AI "fix" `engine.py` | The checker warns that `engine.py` has changed. Your B1 row scores 0. | Put back the kit's `engine.py`. Change `game.py` or a display instead. |
| Asking AI to "improve the story" | Story text you did not write. An academic-integrity matter. | Write story text yourself. Ask the AI about code only. |
| The `.in` header is missing or misspelled | `FAIL story_escaped: the .in file needs a header like '# story: stories/toy.json seed: 1'` | First line exactly: `# story: stories/story.json seed: 1` |
| No `q` at the end of the `.in` | The run ends at "r = play again, q = quit" and quits at the end of input. It works, but it is easy to misread. | End every `.in` with `q`. |
| Running `--regen` and not reading the diff | A test that "passes" because it now records the bug. | Read every changed `.out` before you commit. |
| A new `.py` file with `class` or `global` | `FAIL no_class_or_global` | Use functions and dicts, as in the kit. |
| Forgetting to log a prompt | `prompts.md` and the disclosure do not match (rubric row E1). | Log each prompt as you send it. |
| Running from the wrong folder | `FileNotFoundError` or `No such file` | `cd cyoa_kit` first. |

---

## Checklist (by the end of Tue 12/1)

- [ ] The blueprint gate commit exists.
- [ ] US-F is in `blueprint.md`, with a check.
- [ ] My tutor says it is on Rung 4.
- [ ] My feature works, and I can explain every line I kept.
- [ ] `engine.py`, `checker.py` and `tests/run_tests.py` are unchanged.
- [ ] At least 3 golden runs, one per ending I claim. Each `.out` ends at its ending.
- [ ] `python3 tests/run_tests.py` prints `ALL TESTS PASSED`.
- [ ] `prompts.md` has every prompt, numbered and dated.
- [ ] `AI-DISCLOSURE.md` has a row for each file or feature AI helped with.

## Exit check

1. Name the three frozen files. Why are they frozen?
2. Copy one line of your feature that AI helped with. Explain it in one sentence.
3. What does `--regen` do, and what must you do right after it?
