# P5LAB3: Refactor, and prove nothing changed

**Date:** Tue 10/27/26 · **Spine module:** M6 Functions · **PRIMM focus:** Modify, Make

> **AI today: Rung 3. AI as reviewer.**
>
> | You may | You may not |
> |---|---|
> | **After** your refactor works and `diff` shows no difference, ask AI to critique it. | Ask AI to write the refactor. |
> | Use a change it suggests, if you understand it. | Use a change you cannot explain. |
>
> "Improvements must be understood and documented (brief note: what changed and why)." Your note goes at the top of your file.

**Goal.** You turn a working lab into functions, and you **prove** with `diff` that the output did not change.

**Demo files** (in `course-cti110-26fa`):

| File | What it is |
|---|---|
| `p3lab_norris.py` | P3LAB, Making Change. The same coin block is pasted five times. |
| `p5/p5lab3_norris.py` | The refactor: `get_cents()`, `count_coins(cents, size)`, `show_count(count, singular, plural)`, `main()`. |
| `p5/p5lab3_input.txt` | One line: `2.91`. The typed answer, saved in a file. |

---

## Words for today

| Word | Means |
|---|---|
| **refactor** | Change how code is written without changing what it does. |
| **input file** | The answers you would type, saved in a file, one per line. `<` feeds it to the program. |
| **`diff`** | Compares two files line by line. **No output means no difference.** |
| **golden run** | A saved input and its exact output. The final project uses these. |

---

## 1. Predict

Open `p3lab_norris.py` and `p5/p5lab3_norris.py` side by side.

1. With input `2.91`, write the full output of `p3lab_norris.py`.
2. `count_coins(291, 100)` returns two values. What are they?
3. `show_count(0, "dime", "dimes")` prints what?
4. The refactor keeps `print("That's", cents,"cents.")` with odd spacing. Why not tidy it?

<details><summary>Answers</summary>

1. `Enter dollars and cents (ex: 2.91): That's 291 cents.` then `2 dollars`, `3 quarters`, `1 dime`, `1 nickel`, `1 penny`, one per line. (With piped input, the prompt and the first line share a line.)
2. `2` and `91`: two dollars, 91 cents left.
3. Nothing. Zero coins print nothing, as in P3LAB.
4. The goal is the **same** output. `print` puts one space between items however you space the commas, so the output is the same. But a refactor is not the time to tidy anything that could change the output. Change one thing at a time; prove it; then change the next.

</details>

## 2. Run: the diff proof

From the repo folder (`course-cti110-26fa`):

```
python3 p3lab_norris.py < p5/p5lab3_input.txt > before.txt
python3 p5/p5lab3_norris.py < p5/p5lab3_input.txt > after.txt
diff before.txt after.txt
```

5. What did `diff` print?
6. Try four more amounts. Change the input file each time, or use `printf`:

```
printf '0.41\n' | python3 p3lab_norris.py > before.txt
printf '0.41\n' | python3 p5/p5lab3_norris.py > after.txt
diff before.txt after.txt
```

| Amount | `diff` printed nothing? |
|---|---|
| `2.91` | |
| `0.01` | |
| `1.00` | |
| `0.41` | |
| `3.66` | |

7. Break it on purpose. In `p5lab3_norris.py`, change `"pennies"` to `"pennys"`. Run the proof with `0.02`. What does `diff` print? Put it back.

<details><summary>Answers</summary>

5. Nothing. The outputs are the same, byte for byte.
6. All five print nothing.
7. Two lines, one from each file:
   ```
   2c2
   < 2 pennies
   ---
   > 2 pennys
   ```
   `<` is a line from the first file, `>` from the second. `2c2` means "line 2 changed".

</details>

## 3. Investigate

8. Find the line in `main()` that catches the two values from `count_coins`. Why does it say `dollars, cents = ...` and not `dollars, leftover = ...`?
9. Pennies use `count_coins(cents, 1)`. What is the leftover after that? Why call it at all?
10. How many lines long is the coin part of `p3lab_norris.py`? Of `main()` in the refactor?

<details><summary>Answers</summary>

8. `cents` must shrink for the next coin. Saving the leftover back into `cents` does that. With `leftover`, `cents` would never change, and every coin would be counted from the full amount.
9. Always 0. It keeps all five coins in one pattern, so the code reads the same every time.
10. About 50 lines against about 15. Same output.

</details>

## 4. Modify

Refactor **your own** P3LAB or P4LAB2 into functions.

- Before you change anything, save a golden run: make an input file, run your old file, save `before.txt`.
- Change one block into one function. Run the proof. Repeat.

## 5. Make: the review (Rung 3)

Only when your refactor runs **and** `diff` prints nothing:

11. Ask an AI to review your file. A good prompt: "Review this refactor for readability. Do not rewrite it. List at most three suggestions."
12. Write a two-line note as a comment block at the top of your file: what you changed because of the review, and why. **Or** what you did not change, and why. See the example at the top of `p5/p5lab3_norris.py`.
13. If you kept a change, run the `diff` proof again.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Tidying output while refactoring (a new space, a new word) | `diff` prints a line with `<` and `>`. | Put the output back exactly. Refactor first; improve later, in a separate step. |
| Not saving the leftover: `dimes, left = count_coins(cents, 10)` | Every coin is counted from the full amount. Wrong counts. | `dimes, cents = count_coins(cents, 10)` |
| The function prints instead of returning | The caller gets `None`. `TypeError: cannot unpack non-iterable NoneType object`. | `return count, leftover` |
| Running from the wrong folder | `No such file or directory: 'p5/p5lab3_input.txt'` | Run from the repo folder, or fix the path. |
| Forgetting `< input.txt` | The program waits for you to type. | Add `< p5/p5lab3_input.txt`. |
| Asking AI before it works | You cannot tell whether a suggestion broke it. | Get the `diff` proof first. Then review. |
| Keeping a suggestion you cannot explain | You will be asked about it. | Use only what you can explain in your note. |

---

## Turn in

- [ ] `p5lab3_<lastname>.py`: your old lab, now in functions, with `main()` at the bottom.
- [ ] Your input file.
- [ ] Proof: `diff` prints nothing. (A screenshot, or paste the commands and say "no output".)
- [ ] The two-line review note as a comment block at the top.

## Exit check

1. `diff before.txt after.txt` prints nothing. What does that prove? What does it **not** prove?
2. Why must the AI review come **after** the proof?
3. A function needs to hand back two numbers. Write the `return` line and the line that catches them.
