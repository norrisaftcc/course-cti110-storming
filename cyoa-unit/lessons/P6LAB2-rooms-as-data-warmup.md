# P6LAB2: Warm-up, rooms as data

**Date:** Thu 11/05/26 (about 30 minutes, inside the existing AI-tools module) · **Spine module:** M7 Structured Data (preview) · **PRIMM focus:** Predict, Run, Investigate

> **AI today: Rung 2. AI as explainer, not author.**
>
> | You may | You may not |
> |---|---|
> | Ask your tutor (set up in P6LAB1) to explain a line or a concept. | Submit code it wrote. |
> | Ask "what does this line do, step by step?" | Ask it to change the program. Today we only read. |
>
> Why: "Reading explanations builds the verification muscle."

**Goal.** You can read a dictionary of dictionaries and follow how one loop uses it to move between rooms.

**Demo file** (in `course-cti110-26fa`): `p6/p6lab2_rooms_norris.py`. Three Fort rooms as data. Read it; do not change it.

---

## Refresher: you have seen this before

| You met | In | Today |
|---|---|---|
| A dictionary: keys and values in `{ }` | `p2/p2lab2_norris.py` (cars and their mpg) | Each room is a dictionary. |
| A list: values in `[ ]`, counted from 0 | `p2/p2hw2_setup.py` (a list of grades) | The numbered exits are a list. |

New today: a dictionary can hold **other** dictionaries. `ROOMS["tower"]` is a whole room. `ROOMS["tower"]["title"]` is that room's title.

---

## 1. Predict

Read the `ROOMS` dictionary at the top of the file. Do not run it yet.

1. What does `ROOMS["jetty"]["title"]` hold?
2. How many exits does the tower have? What are their labels?
3. What is the **first** thing the program prints (after an empty line)?
4. You type `1`, then `2`, then `q`. Which rooms do you see, in order?

<details><summary>Answers</summary>

1. `"S1. The Broken Jetty"`
2. Two: `Walk down to the jetty` and `Look in the cottage`.
3. `S1. The Broken Jetty`. The loop starts with `room = "jetty"`.
4. The jetty, the tower (exit 1 from the jetty), the cottage (exit 2 from the tower). Then `You row home.`

</details>

## 2. Run

```
cd p6
python3 p6lab2_rooms_norris.py
```

5. Check your answers. Then type `5` at the tower. What happens? Why?

<details><summary>Answers</summary>

5. `That is not on the list.` The tower has two exits, so `valid` is `["q", "1", "2"]`. `"5"` is not in it, so the `while` loop asks again.

</details>

## 3. Investigate (with your tutor)

6. `here = ROOMS[room]`. What kind of value is `here`? (A string? A list? A dictionary?)
7. `for target in here["exits"]:` What values does `target` take at the tower? Is it the ids or the labels?
8. `room = targets[int(answer) - 1]`. Why `- 1`?
9. Why is `answer` checked against a list of **strings** (`"1"`, `"2"`), not numbers?
10. Pick **two** lines you do not fully understand. Ask your tutor to explain each one. Then write each explanation **in your own words**, one or two sentences. Do not paste the tutor's words.

| Line | My explanation, in my own words |
|---|---|
| | |
| | |

<details><summary>Answers to 6-9</summary>

6. A dictionary: the room's own dict with `title`, `text` and `exits`.
7. The **ids**: `"jetty"`, then `"cottage"`. A `for` loop over a dict gives its keys.
8. People count from 1. Lists count from 0. Exit 1 is `targets[0]`.
9. `input()` always returns a string. The program compares strings first, and only turns the answer into a number with `int()` once it knows it is valid.

</details>

## 4. Modify and 5. Make

Not today. In P7LAB1 you will add rooms and a character sheet.

---

## Common mistakes (when you read and run dicts)

| Mistake | What you see | Fix |
|---|---|---|
| A key with a typo: `ROOMS["towr"]` | `KeyError: 'towr'` | Copy the key exactly. Keys are case-sensitive. |
| Missing quotes: `here[title]` | `NameError: name 'title' is not defined` | `here["title"]` |
| Same quotes inside an f-string: `f"{here["title"]}"` | A `SyntaxError` on Python 3.11 and older. | Use the other kind inside: `f"{here['title']}"` |
| Forgetting `- 1` | The wrong room, or `IndexError: list index out of range` | `targets[int(answer) - 1]` |
| `int(answer)` before checking it | `ValueError: invalid literal for int()` when someone types `x` | Validate first, then convert. |
| Pasting the tutor's answer as your explanation | You cannot explain it next week. | Close the chat. Write it from memory. |

---

## Turn in

- [ ] Your Predict answers (1-4), written **before** you ran it.
- [ ] Your two lines and your own-words explanations (question 10).

## Exit check

1. In `ROOMS["cottage"]["exits"]`, what is the key and what is the value?
2. Why does a `for` loop over `here["exits"]` give room ids, not labels?
