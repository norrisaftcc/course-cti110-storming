# P5LAB2: Parameters and return

**Date:** Thu 10/22/26 · **Spine module:** M6 Functions · **PRIMM focus:** Investigate, Modify

> **AI today: Rung 2. AI as explainer, not author.**
>
> | You may | You may not |
> |---|---|
> | Ask AI to explain an error message or a concept. Today's best question: "Explain this traceback in plain words." | Submit code it wrote. |
>
> Why: "Submitting generated code while learning syntax is lifting with a forklift."

**Goal.** You can pass a value into a function, hand a value back with `return`, and use the result.

**Demo files** (in `course-cti110-26fa`):

| File | What it is |
|---|---|
| `p5/p5lab2_trap_norris.py` | **The trap.** Rooms call rooms. The calls pile up until Python stops the program. |
| `p5/p5lab2_norris.py` | **The fix.** Each room returns the next room's id. One loop moves the hero. |

---

## Words for today

| Word | Means | Example |
|---|---|---|
| **parameter** | A name in the `def` line. It waits for a value. | `def jetty(hero_name):` |
| **argument** | The value you pass in the call. | `jetty("Mira")` |
| **return** | Hand a value back to the caller. The function stops there. | `return "tower"` |
| **room id** | A short string that names a room. | `"docks"`, `"jetty"`, `"tower"`, `"cottage"` |

---

## The trap, in plain words

In M3BONUS each door was a function. That was good. The trap comes next: a room function that **calls** the next room function.

- `jetty()` calls `tower()` to walk up.
- `tower()` calls `jetty()` to walk back down.

Each call starts **inside** the one before it. The old call never ends. It waits. Walk back and forth, and the waiting calls pile up like plates. Python allows about 1,000. Then it stops the program:

```
RecursionError: maximum recursion depth exceeded
```

There is a second, quieter problem. Any line written **after** a room call waits too. It runs later, when the calls unwind, in reverse order. The player sees text they did not expect.

## The fix, in plain words

A room never calls a room. A room **returns the id of the next room**, as a string. One loop in `main()` moves the player:

```python
room = "docks"
while room != "end":
    if room == "docks":
        room = docks(hero_name)
    elif room == "jetty":
        room = jetty(hero_name)
    ...
```

Each room finishes before the next one starts. The calls never pile up. This is the shape of the kit's game loop, and of almost every game loop you will meet.

---

## 1. Predict

Open `p5/p5lab2_trap_norris.py`. Read the comment block at the top and both room functions.

1. You type `walk`, then `y`, `y`, `y`, `n`. Which rooms do you see, and what `calls deep` number does each one show?
2. After the last `n`, which lines print, and in what order?
3. You type `auto`. Roughly how deep will the calls get before Python stops?

<details><summary>Answers</summary>

1. Jetty (calls deep: 1), Tower (2), Jetty (3), Tower (4).
2. `(late line: jetty at depth 3 ends now)`, then `(late line: jetty at depth 1 ends now)`, then `The walk is over.` The late lines print in **reverse** order, as each waiting call ends.
3. A little under 1,000. On Python 3.13 the last room shows `calls deep: 998`. Your number may differ by a few.

</details>

## 2. Run

```
cd p5
printf 'walk\ny\ny\ny\nn\n' | python3 p5lab2_trap_norris.py
python3 p5lab2_trap_norris.py
```

For the second run, type `auto`. Let it scroll.

4. Read the traceback together. What is its **first** line? What is its **last** line? Which two lines of code repeat in the middle?

<details><summary>Answers</summary>

4. First: `Traceback (most recent call last):`. Last: `RecursionError: maximum recursion depth exceeded`. The two lines that repeat are `tower(depth + 1, auto)` in `jetty()` and `jetty(depth + 1, auto)` in `tower()`: each room calling the other.

</details>

## 3. Investigate

5. In the trap file, find the line that calls a room from inside a room. Mark it.
6. Find the **late line**. Why does it run late?
7. Now open `p5/p5lab2_norris.py`. Where does the next room come from? Point to the exact line in `main()`.
8. What does `jetty()` return if the player picks 2?
9. `tick(turn, torch)` returns two values. Find the line that catches them. What would happen if you wrote only `tick(turn, torch)`?
10. Run the fix: `printf 'Mira\ny\n1\n2\n3\n' | python3 p5lab2_norris.py`. Does the call pile grow? How do you know?

<details><summary>Answers</summary>

5. `tower(depth + 1, auto)` inside `jetty()`, and `jetty(depth + 1, auto)` inside `tower()`.
6. It is written after a room call. It cannot run until that call, and every call inside it, has ended.
7. `room = jetty(hero_name)` (and the same for each room). The room returns a string; `room =` saves it.
8. `"end"`. The loop test `room != "end"` is then false, and the loop stops.
9. `turn, torch = tick(turn, torch)`. Without `turn, torch =`, the new values are thrown away. The turn never goes up and the torch never burns.
10. No. Each room returns before the next one is called. There is no `calls deep` number to grow, and no late lines.

</details>

## 4. Modify

Work in a copy: `cp p5lab2_norris.py p5lab2_mine.py`.

11. **Add a room.** Write `cellar(hero_name)`. Print:

    ```
    C1. THE CELLAR STAIR
    Twenty feet down, an oak door. It is stuck.
    ```

    Give two choices: climb back up (return `"tower"`) or row home (return `"end"`). In `tower()`, make choice 3 return `"cellar"`. Add an `elif` for it in `main()`.
12. **Break it on purpose.** In `cottage()`, delete `return "tower"`. Run and visit the cottage. What happens? Why? Put it back.
13. **Break it again.** In `main()`, change `room = jetty(hero_name)` to just `jetty(hero_name)`. What happens? Put it back.

<details><summary>Answers</summary>

12. The cottage returns `None`. No `if` or `elif` matches `None`, so no room runs. But the loop keeps going, and the clock keeps ticking: `Turn 4`, `Turn 5`, `Turn 6`, until the torch dies and the game ends.
13. `room` stays `"jetty"`. You see the jetty again, and again, until the torch dies.

</details>

## 5. Make

Write `p5lab2_<lastname>.py`, your own small map:

- At least three rooms. Each takes **one parameter** and **returns** the next room id.
- One `while room != "end":` loop in `main()`. No room calls another room.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| A room calls the next room: `tower(name)` inside `jetty()` | It works for a while. Lines after the call run late. Then `RecursionError: maximum recursion depth exceeded`. | `return "tower"`. Let the loop in `main()` make the call. |
| Forgetting `return` | The room hands back `None`. No branch matches. The loop spins (here: the turns tick until the torch dies). | Every path through a room must `return` a room id or `"end"`. |
| Calling a room and not saving the result: `jetty(name)` | `room` never changes. The same room shows again and again. | `room = jetty(name)` |
| A typo in a returned id: `return "towr"` | Same as no return: no branch matches. | Copy the id from the `elif` line. Ids are case-sensitive. |
| `tick(turn, torch)` without using the result | `turn` and `torch` never change in `main`. | `turn, torch = tick(turn, torch)` |
| Mixing up argument order | The function gets the wrong value in each parameter. | Arguments match parameters by position. |
| Printing the next room instead of returning it | The id shows on screen; the loop gets `None`. | `return` the value; let the caller use it. |

---

## Turn in

- [ ] `p5lab2_<lastname>.py` with the class header.
- [ ] At least three rooms, each with one parameter.
- [ ] Each room returns the next room id, or `"end"`.
- [ ] One `while` loop in `main()` moves the player. No room calls a room.
- [ ] `main()` is the last line.

## Exit check

1. What does `return "tower"` do? Where does the string `"tower"` go?
2. Why does the trap file crash after about 1,000 moves, but the fixed file never does?
3. A room forgets its `return`. What value does the loop get?
