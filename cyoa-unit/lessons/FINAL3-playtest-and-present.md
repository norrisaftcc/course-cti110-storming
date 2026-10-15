# FINAL3: Playtest and present

**Dates:** Thu 12/3/26 (playtest and rehearsal) · Tue 12/8/26 and Thu 12/10/26 (presentations) · Packet due Thu 12/10/26, 11:59 pm · **Spine module:** M8 Programming Miniproject · **PRIMM focus:** none (verify and communicate)

> **AI today: Rung 4 for fixes on 12/3. None in the presentation.**
>
> | You may | You may not |
> |---|---|
> | On 12/3, use your Rung 4 tutor to help fix a bug your tester found, in your feature's code. | Ask AI to rewrite story text your tester found confusing. You fix your own words. |
> | Use your own notes when you present. | Read an AI's explanation aloud as your answer. |
>
> The Ladder: "The presentation is the audit. A student who cannot explain their own software fails the presentation regardless of whether the software runs."

**Goal.** A classmate plays your game and you fix what confused them. Then you show your game, your map, one user story with its check, and one line of your feature, and you answer questions in your own words.

**Files:** your `cyoa_kit/`, your `stories/blueprint.md`, and the playtest form below (print it, or copy it into `playtest.md`).

---

## Words for today

| Word | Means |
|---|---|
| **playtest** | Someone else plays your game while you watch and say nothing. |
| **confusing spot** | A place where the tester stopped, guessed, or asked "what do I do?". |
| **Definition of Done** | The four lines in `ASSIGNMENT.md` section 5. The playtest is the last one. |
| **the audit** | The presentation. It checks that you understand what you hand in. |

---

## 1. Playtest (Thu 12/3, 30 minutes)

Pair up. Each of you plays the other's game. Then swap.

**The tester:**

1. Play with the plain display: `python3 game.py stories/story.json`.
2. Think out loud. Say what you expect before you pick.
3. Play to at least **two different endings**. Use `r` to restart.
4. Fill in the form. Sign it.

**The author:**

1. Sit on your hands. Say nothing while they play. Write down every place they stop or guess.
2. After, ask: "What did you think the lever would change?"
3. Make **one fix** for the most confusing spot, or write a note on why you will not.
4. If you changed story text or output: `python3 tests/run_tests.py --regen`, read the diff, then `python3 tests/run_tests.py`.

1. Your tester says, "I didn't know the Wizard choice mattered." Is that a bug in your code or in your story? Where would you fix it?

<details><summary>Answer</summary>

1. In the story. The code did what the story said. Fix the `sub` line under the choice (for example, "A dagger and one Sleep spell.") or a beat that hints at what the choice changes. You write the fix yourself, then run `--regen` and read the diff.

</details>

### The playtest form

Print one per tester, or copy it into `cyoa_kit/playtest.md`. A photo of the signed form in your repository is fine.

```
CTI 110 FINAL PROJECT: PEER PLAYTEST FORM                 Date: ____________

Author: ______________________   Story title: ______________________________

Tester: ______________________

ENDINGS THE TESTER REACHED (at least 2)
  1. Ending title: ____________________   Role chosen: __________________
  2. Ending title: ____________________   Role chosen: __________________
  3. Ending title: ____________________   Role chosen: __________________

DID THE LEVER MATTER?  (tester answers)
  What did your choice of role change? ______________________________________
  ___________________________________________________________________________

ONE CONFUSING SPOT  (tester answers)
  Scene or question: ________________________________________________________
  What was confusing: _______________________________________________________
  ___________________________________________________________________________

ONE FIX MADE, OR A NOTE  (author answers)
  [ ] I made this fix:  ______________________________________________________
      Commit message: ________________________________________________________
  [ ] I did not fix it, because: _____________________________________________
  ___________________________________________________________________________

  After the fix: run_tests.py printed ALL TESTS PASSED   [ ] yes   [ ] no fix made

SIGNATURES
  Tester: ______________________________   Author: ____________________________
```

---

## 2. Rehearse (Thu 12/3, the rest of class)

Time yourself. Five minutes is short. Use the checklist below.

Open these before you start, so you never search for a file in front of the class:

| Window | What it shows |
|---|---|
| A terminal in `cyoa_kit/` | Ready to type `python3 game.py stories/story.json` |
| `stories/blueprint.md` on GitHub | Your Mermaid map, drawn, and your user stories |
| A second terminal in `cyoa_kit/` | Ready to type `python3 tests/run_tests.py` or the checker |
| Your feature's code | Open at the line you will explain |

---

## 3. Present (Tue 12/8 or Thu 12/10)

**5 minutes, then questions.**

### Presentation checklist

| Done | Part | Time | What you do |
|---|---|---|---|
| [ ] | **Play it live** | 1.5 min | Run your game. Play one golden run to its ending. When you choose your role, say what the lever is and what it changes. |
| [ ] | **The map** | 0.5 min | Show the Mermaid map. Trace the path you just played. |
| [ ] | **One user story with its check** | 1 min | Read one user story and its Given/When/Then. Show its check passing: the checker line, or `run_tests.py` printing `PASS story_<ending>`. |
| [ ] | **One line of your feature** | 1.5 min | Show your feature working. Point at one line. Say what it does, why it is there, and what would break without it. |
| [ ] | **One cut** | 0.5 min | Name one thing on your cut list and why you cut it. |
| [ ] | **Questions** | 2 to 3 min | Answer in your own words. "I don't know; here is how I would find out" is a good answer. |

**A student who cannot explain their own software fails the presentation.** It does not matter who typed the code.

### Sample questions

The instructor and classmates may ask questions like these. Practise two of them out loud with a partner.

1. Show me where your lever is set in `story.json`. Which option only one role can see?
2. Which choice in your story is a real decision? Which ending does it close off?
3. Pick one flag. Where is it set, and what does it open?
4. Why can the AI not change `engine.py` in this project? What would break if it did?
5. What does `--regen` do? When did you last run it, and what did the diff show?
6. Your feature: what happens if the player presses that key at an ending, or before any choice?
7. What did you ask an AI for that you rejected? Why?
8. Pick one item on your cut list. What would have to be true for you to add it back?

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Helping the tester while they play | The form says "no confusing spots", and the class finds three. | Say nothing. Write down where they stop. |
| Fixing story text and not running the tests | Golden runs fail at the deadline. | `--regen`, read the diff, run the tests, commit. |
| A demo that starts with "wait, where is my file?" | A minute lost. | Open every window before your turn. |
| Explaining the whole feature line by line | You run out of time. | One line. What, why, and what breaks without it. |
| Answering a question you do not know with a guess | The next question digs into the guess. | Say what you would run or read to find out. |
| Turning in without the signed form | Rubric row C2 scores 0, and the Definition of Done is not met. | Add a photo of the form to the repository. |

---

## Checklist: the packet (due Thu 12/10/26, 11:59 pm)

- [ ] `stories/story.json`: the checker prints `RESULT: PASS`.
- [ ] `stories/blueprint.md`: all ten sections, US-F, and dated notes for changes after the gate.
- [ ] At least 3 golden runs, `tests/story_<ending id>.in` and `.out`.
- [ ] My feature, in `game.py`, a `display_*.py` file or a new `.py` file.
- [ ] `python3 tests/run_tests.py` prints `ALL TESTS PASSED`.
- [ ] `prompts.md` and `AI-DISCLOSURE.md`.
- [ ] The signed playtest form, with one fix or a note.
- [ ] Pushed to GitHub, and the link turned in.

## Exit check

1. What was your tester's confusing spot, and what did you do about it?
2. Which line of your feature will you explain? Write the one-sentence version now.
3. Which of the 8 sample questions would be hardest for you? What will you read tonight to be ready?
