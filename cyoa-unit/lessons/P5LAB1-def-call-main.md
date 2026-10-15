# P5LAB1: def, call, main()

**Date:** Tue 10/20/26 · **Spine module:** M6 Functions · **PRIMM focus:** Predict, Run, Investigate

> **AI today: Rung 2. AI as explainer, not author.**
>
> | You may | You may not |
> |---|---|
> | Ask AI to explain an error message or a concept. | Submit code it wrote. |
> | Ask "what does `def` do?" or "why is this a NameError?" | Ask it to write your functions for you. |
>
> Why: "Submitting generated code while learning syntax is lifting with a forklift." Turn off Copilot's inline suggestions for today.

**Goal.** You can write a function with no parameters, call it, and start a program from `main()` at the bottom of the file.

**Demo files** (in `course-cti110-26fa`):

| File | What it is |
|---|---|
| `p5/p5lab1_before_norris.py` | A short walk on the Isle of Old Stone, written top to bottom. Two blocks are pasted three times. |
| `p5/p5lab1_norris.py` | The same walk with functions. The output is exactly the same. |

---

## Words for today

| Word | Means |
|---|---|
| **function** | A block of code with a name. |
| **define** | Write the function with `def`. Nothing runs yet. Python just learns the name. |
| **call** | Run the function: its name, then `()`. Example: `show_help()`. |
| **`main()`** | The function where the program starts. It reads like a table of contents. |

---

## 1. Predict (before you run anything)

Open `p5/p5lab1_before_norris.py`. Read it. Do **not** run it yet. Write your answers on paper.

1. How many times does the help block (the three lines that start with `-`) print?
2. How many times does the line `THE FIRST DELVE` print?
3. The program asks for one thing. What is it?
4. You type `Mira`. Write the first two lines of output.

<details><summary>Answers</summary>

1. Three times. It is pasted three times.
2. Three times. The banner is pasted three times too.
3. The hero's name.
4. `What is your hero's name? Mira` (you typed `Mira`), then `Hero: Mira`.

</details>

## 2. Run

```
cd p5
python3 p5lab1_before_norris.py
```

5. Were your answers right? Circle any you missed. Write one sentence on why.

## 3. Investigate

Now open `p5/p5lab1_norris.py`. It prints the same thing.

6. Find every `def`. How many functions are there? Write their names.
7. Find every **call** of `show_help`. How many are there?
8. The file starts with five `def` blocks. Does anything print while Python reads them? Why or why not?
9. Why is `main()` the **last** line of the file?
10. Try it. Cut the last line, `main()`, and paste it at the very top, above every `def`. Run. What happens? Put it back.
11. Now leave `main()` at the bottom, but move the whole `def show_help():` block below it, to the very end of the file. Run. What happens? Put it back.
12. Prove the two files print the same thing:

```
printf 'Mira\n' | python3 p5lab1_before_norris.py > before.txt
printf 'Mira\n' | python3 p5lab1_norris.py > after.txt
diff before.txt after.txt
```

What does `diff` print? What does that mean?

<details><summary>Answers</summary>

6. Six: `show_divider`, `show_help`, `describe_docks`, `describe_jetty`, `describe_tower`, `main`.
7. Three, all inside `main()`.
8. No. `def` only defines. Nothing runs until a call.
9. Python reads the file from top to bottom. By the last line, every function is defined. So `main()` can call any of them.
10. `NameError: name 'main' is not defined`. Python has not reached `def main():` yet, so the name does not exist.
11. `NameError: name 'show_help' is not defined`. `main()` runs before Python has read `def show_help():`. The rule: a function must be defined above the line that **runs** the call.
12. Nothing. No output from `diff` means the two files are the same, byte for byte.

</details>

## 4. Modify

13. Add a function `describe_cottage()`. Use this text:

    ```
    S3. THE KEEPER'S COTTAGE
    No roof. Ash in the hearth, less than a week old. A tin of lamp
    oil. On the door, a chalked eye with a line through it.
    ```

14. Call it from `main()` after the tower, with `show_divider()` before it and `show_help()` after it.
15. Change one word in `show_help()`. Run. How many places in the output changed? How many places in the **before** file would you have to change?

## 5. Make

Write `p5lab1_<lastname>.py`. Your own short walk, three or more places. Your own text is fine.

- At least three named functions, plus `main()`.
- One function is called more than once.
- `main()` is called on the last line, with the comment `# at the bottom -- start the program`.

---

## Common mistakes

From the Fort classroom's stage 3 and stage 4 tables (Python rows only), plus one for today.

| Mistake | What you see | Fix |
|---|---|---|
| `main()` called above the `def`s | `NameError: name 'main' is not defined` | Call `main()` on the last line of the file. |
| Calling without the parentheses: `show_help` | Nothing prints. Python names the function but does not run it. (In an `if`, `if check:` is always true.) | `show_help()` |
| Forgetting `return` | The function hands back `None`, which counts as false. | Every path through the function must `return` a value. (More in P5LAB2.) |
| Printing inside a function when you meant to return | The value is shown, not handed back. The caller gets nothing to test. | `return` the value; let the caller print. |
| `tick(turn, torch)` without using the result | `turn` and `torch` never change in `main`. | `turn, torch = tick(turn, torch)` |
| Mixing up argument order: `attack(12, 1)` | Bonus 12 against AC 1: every swing hits. | Arguments match parameters by position. |
| `turn + 1` instead of `turn = turn + 1` | Nothing changes. The sum is thrown away. | `turn = turn + 1` |
| Reading input outside the loop | The loop uses the same answer forever. | Read the input inside the loop. |
| The loop variable never changes | The loop never ends. | Make sure some path inside the loop makes the test false, or returns. |

---

## Turn in

- [ ] `p5lab1_<lastname>.py` with the class header (`# CTI 110`, `# P5LAB1 - Functions`, your name, the date).
- [ ] At least three functions and a `main()`.
- [ ] One function is called more than once.
- [ ] `main()` is the last line.
- [ ] It runs with no errors.

## Exit check

1. What is the difference between **defining** a function and **calling** it?
2. You see `NameError: name 'show_map' is not defined`. Name two causes.
3. Why does a function you call three times save you work when the text changes?
