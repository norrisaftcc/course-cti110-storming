# P7LAB1: The dispatch loop and the character sheet

**Date:** Tue 11/10/26 · **Spine module:** M7 Structured Data · **PRIMM focus:** Investigate, Modify

## Start of class: swap your tutor to Rung 3

Today your AI tutor moves up one rung, from explainer to reviewer. It is one command, run from the root of your repository. See `ai-tutor/README.md` for the command. Then ask your tutor: "What rung are you on?" It should say Rung 3.

> **AI today: Rung 3. AI as reviewer.**
>
> | You may | You may not |
> |---|---|
> | **After** your program works, ask AI to critique it. | Ask AI to write the room functions or the loop. |
> | Ask AI to explain an error or a concept (still fine). | Use a change you cannot explain. |
>
> "Improvements must be understood and documented (brief note: what changed and why)."

**Goal.** You can store a character sheet in a dictionary, store functions in a dictionary, and move the player with one line: `room = ROOMS[room](hero)`.

**Demo file** (in `course-cti110-26fa`): `p7/p7lab1_norris.py`. The P5LAB2 rooms, a hero dict, and the lever.

---

## Refresher: lists and dictionaries (you met them in P2)

| Idea | You saw it in | Example from today |
|---|---|---|
| A dictionary maps keys to values | `p2/p2lab2_norris.py`: `cars["Prius"]` gives `52.36` | `hero["hp"]` gives `8` |
| Change a value in a dictionary | | `hero["role"] = "wizard"` |
| A list holds values in order | `p2/p2hw2_setup.py`: `grade_list = [grade1, grade2, grade3]` | `hero["items"]` starts as `[]` |
| Add to a list | | `hero["items"].append("oil")` |
| Is it in the list? | | `"oil" in hero["items"]` gives `True` or `False` |

**New today:** a dictionary can hold **functions**. A function name without `()` is the function itself, not a call.

```python
ROOMS = {
    "docks": docks,      # no () -- we store the function
    "jetty": jetty,
    ...
}
room = "docks"
while room != "end":
    room = ROOMS[room](hero)    # look it up, then call it with ()
```

This one line replaces the whole `if`/`elif` chain from P5LAB2. Add a room, add one line to `ROOMS`. The loop never changes.

**The lever.** At the docks you choose the Fighter or the Wizard. The choice is stored as a field: `hero["role"]`. Later, the cellar door tests it. The Fighter forces the door. The Wizard opens it only with oil from the cottage. Your final project will have a lever too.

---

## 1. Predict

Read `p7/p7lab1_norris.py`.

1. What does `hero` hold right after this line: `hero = {"name": name, "role": "", "hp": 0, "items": []}`?
2. You pick the Wizard. What are `hero["role"]` and `hero["hp"]` after `docks()`?
3. A Wizard goes straight to the cellar without visiting the cottage. Which line does option 1 show?

<details><summary>Answers</summary>

1. The name you typed, an empty role, 0 hp, and an empty items list.
2. `"wizard"` and `4`. (The Fighter gets `"fighter"` and `8`.)
3. `1. Push the door (Wizard, no oil)`. Pushing it prints `The door will not move. Oil from the cottage might help.`

</details>

## 2. Run

```
cd p7
python3 p7lab1_norris.py
```

4. Play twice: once as each role. Reach the oil store both times. Write the keys you typed each time.

## 3. Investigate

5. What is `ROOMS["tower"]`? (Not what it **does**: what it **is**.)
6. What does `ROOMS["tower"](hero)` do?
7. Why are there no parentheses inside the `ROOMS` dict?
8. `cottage()` changes `hero["items"]`, but it does not `return` the hero. How does `main()` see the oil? (Hint: there is only one dictionary. Every room gets the same one.)
9. Find each place that tests `hero["role"]`. What would break if the docks stored `"Fighter"` with a capital F?

<details><summary>Answers</summary>

5. The `tower` function itself.
6. It looks up the `tower` function and calls it, passing `hero`. The room returns the next room id, and `room =` saves it.
7. With `()`, Python would **call** each room while it builds the dictionary. With no argument it fails: `TypeError: jetty() missing 1 required positional argument: 'hero'`.
8. A dictionary is passed to a function as **the same object**, not a copy. When a room changes it, `main()` sees the change.
9. `cellar()` tests it. `"Fighter" == "fighter"` is false, so a Fighter would be treated as a Wizard. Pick one spelling (lowercase) and use it everywhere.

</details>

## 4. Modify

Work in a copy: `cp p7lab1_norris.py p7lab1_mine.py`.

10. **Add a room.** Write `stair(hero)` for the top of the tower stair. It prints one line and returns `"tower"`. Add a choice in `tower()` that returns `"stair"`. Add **one line** to `ROOMS`. Did you need to touch the loop?
11. **Add an item, test it elsewhere.** In your new room, offer the hero a `"rope"`. Append it to `hero["items"]`. Then, in `jetty()`, print a new line only when `"rope" in hero["items"]`.
12. **Break it on purpose.** Make a room return `"towr"`. Run. Read the error. Put it back.

<details><summary>Answer to 12</summary>

12. `KeyError: 'towr'`. The loop looks up `ROOMS["towr"]`, and there is no such key.

</details>

## 5. Make

Write `p7lab1_<lastname>.py`:

- A `hero` dictionary with at least `name`, `role`, `hp` and `items`.
- At least four rooms in a `ROOMS` dictionary, moved by `room = ROOMS[room](hero)`.
- A lever: one early choice sets `hero["role"]`, and a later room offers something only one role sees.
- One item added in one room and tested in another.

Then the Rung 3 review: ask AI to critique it **after** it works. Add a two-line note at the top: what you changed and why, or what you did not change and why.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `()` inside the dict: `"jetty": jetty()` | `TypeError: jetty() missing 1 required positional argument: 'hero'` | `"jetty": jetty` |
| A new room not added to `ROOMS` | `KeyError: 'stair'` | Add `"stair": stair,` to `ROOMS`. |
| A typo in a returned id: `return "towr"` | `KeyError: 'towr'` | Copy the id from `ROOMS`. |
| A room forgets `return` | `KeyError: None` | Every path returns a room id or `"end"`. |
| Missing quotes: `hero[role]` | `NameError: name 'role' is not defined` | `hero["role"]` |
| `hero["items"] = "oil"` | The list is gone. `items` is now a string. | `hero["items"].append("oil")` |
| `"Fighter"` in one place, `"fighter"` in another | The role test is never true. | One spelling, lowercase, everywhere. |

---

## Turn in

- [ ] `p7lab1_<lastname>.py` with the class header.
- [ ] A `hero` dict, a `ROOMS` dict, and the one-line dispatch loop.
- [ ] A lever: an option only one role sees.
- [ ] An item set in one room and tested in another.
- [ ] The two-line Rung 3 review note at the top.

## Exit check

1. What is the difference between `jetty` and `jetty(hero)`?
2. You add a room function but forget its line in `ROOMS`. What error do you see, and when?
3. What is the lever in the demo, and which room tests it?
