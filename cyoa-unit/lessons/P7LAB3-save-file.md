# P7LAB3: Save and load a character

**Date:** Tue 11/17/26 · **Spine module:** M7 Structured Data · **PRIMM focus:** Modify, Make

> **AI today: Rung 3. AI as reviewer.**
>
> | You may | You may not |
> |---|---|
> | **After** your save and load work, ask AI to critique your code. | Ask AI to write `save_hero` or `load_hero` for you. |
> | Ask AI to explain an error, such as the `TypeError` below. | Use a change you cannot explain. |
>
> "Improvements must be understood and documented (brief note: what changed and why)."

**Goal.** A program can stop and start again where it left off. You save a character sheet to a JSON file and load it back, unchanged.

**Demo file** (in `course-cti110-26fa`): `p7/p7lab3_norris.py`. It saves a hero dict to `hero_save.json`, loads it back, and checks that the two are equal.

---

## Words for today

| Word | Means |
|---|---|
| **`json.dump(data, file, indent=2)`** | Writes Python data into a file as JSON. `indent=2` makes it easy to read. |
| **`json.load(file)`** | Reads a JSON file back into Python data. |
| **`open(path, "w")`** | Opens a file for **writing**. It makes the file, or replaces what was in it. |
| **`with open(...) as f:`** | Opens the file, and closes it for you at the end of the block. |
| **save file** | The state of a game, written to a file. The kit's is `save_<story id>.json`. |

---

## 1. Predict

Read `p7/p7lab3_norris.py`.

1. What file will the program make? In which folder?
2. What will the last line print?
3. Read the comment block at the bottom. Why can't a `set` be saved as JSON?

<details><summary>Answers</summary>

1. `hero_save.json`, in the folder you run it from (run it from `p7`).
2. `hero == loaded: True`. The loaded dict has the same keys and the same values.
3. JSON has lists, but no sets. `json.dump` stops with `TypeError: Object of type set is not JSON serializable`.

</details>

## 2. Run

```
cd p7
python3 p7lab3_norris.py
```

Open `hero_save.json` in the editor.

4. How does the file show the `items` list? Is it Python, or JSON? How can you tell?

<details><summary>Answer</summary>

4. One item per line, in double quotes, inside `[ ]`. It is JSON: JSON uses only double quotes. (Python's `print` showed single quotes.)

</details>

## 3. Investigate

5. Try the trap. In a scratch file, run:

   ```python
   import json
   flags = {"lamp"}
   json.dump({"flags": flags}, open("bad.json", "w"))
   ```

   Copy the last line of the error. Then change `flags` to `sorted(flags)` and run again. Open the file.
6. Change `"items"` in the demo to a **tuple**: `("torch", "oil")`. Run. What does the last line print now? Why? Put it back.
7. Why does the kit keep its flags as a **sorted** list, not just a list?

<details><summary>Answers</summary>

5. `TypeError: Object of type set is not JSON serializable`. With `sorted(flags)` the file holds `{"flags": ["lamp"]}`.
6. `hero == loaded: False`. JSON has no tuples. The tuple is saved as a list and loads back as a list. A list is not equal to a tuple.
7. A sorted list comes out in the same order every time. So the same game gives the same save file, byte for byte. Golden runs need that.

</details>

## 4. Modify

8. Add a key `"gold"` (a whole number) to the hero. Run. Is it still `True`?
9. Change `main()` so it **loads first** if `hero_save.json` exists, raises `hp` by 1, and saves again. Run it three times. What is `hp` now? (Hint: `import os` and `os.path.exists("hero_save.json")`.)

## 5. Make, then the kit

10. Write `p7lab3_<lastname>.py`: your own character sheet with at least one list in it. Save it, load it back, and print `hero == loaded`.
11. **The kit does the same thing.** Go to the kit and play the Fort story:

    ```
    cd cyoa_kit
    python3 game.py stories/fort.json
    ```

    Make two or three choices. At a choice, press `s` (save). Press `q` (quit).
12. Start it again: `python3 game.py stories/fort.json`. At the first choice, press `l` (load). Where are you?
13. Open `save_fort.json` in the editor. Read it.

| Question | Your answer |
|---|---|
| Which key says where you are? | |
| What is in `fields`? Where did that word come from? | |
| What is in `flags`? Is it a list or a set? | |
| What is `trail`? | |
| How many keys does the file have? | |

<details><summary>Answers to 12-13</summary>

12. At the same scene and the same choice where you pressed `s`.
13. `scene` says where you are (and `group` says which choice in it). `fields` holds `role`, set by your first choice: `fighter` or `wizard`. `flags` is a **sorted list**, for the reason in question 7. `trail` is every scene you entered, in order. Seven keys: `story`, `scene`, `group`, `fields`, `meters`, `flags`, `trail` (STORY-FORMAT.md section 10.1).

</details>

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Saving a set | `TypeError: Object of type set is not JSON serializable` | Save `sorted(flags)`, a list. |
| Arguments swapped: `json.dump(save_file, hero)` | `TypeError: Object of type TextIOWrapper is not JSON serializable` | Data first, then the file: `json.dump(hero, save_file)`. |
| Writing to a file opened without `"w"` | `io.UnsupportedOperation: not writable` | `open(path, "w")` |
| Loading from the wrong folder | `FileNotFoundError: [Errno 2] No such file or directory: 'hero_save.json'` | Run from the folder where you saved it, or check with `os.path.exists`. |
| A tuple in the data | It saves, but loads back as a list. `hero == loaded` is `False`. | Use lists. |
| Editing the save file by hand and breaking it | `json.decoder.JSONDecodeError` when loading | Fix the JSON, or delete the file and save again. |
| Committing your save files to Git | Your repository fills with test saves. | Do not `git add` `hero_save.json` or `save_*.json`. |

---

## Turn in

- [ ] `p7lab3_<lastname>.py` that saves and loads a character with at least one list in it, and prints `hero == loaded: True`.
- [ ] Your answers to the `save_fort.json` table (question 13).
- [ ] The two-line Rung 3 review note at the top of your file.

## P7 exit ticket (end of class)

1. What does `json.dump` do? What does `json.load` do?
2. Why does the kit store flags as a sorted list and not a set?
3. You press `s` in the kit, quit, start again and press `l`. What file did the kit read, and which key told it where you were?
