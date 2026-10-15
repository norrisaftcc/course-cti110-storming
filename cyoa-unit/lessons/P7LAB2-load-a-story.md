# P7LAB2: Load a story from a file

**Date:** Thu 11/12/26 · **Spine module:** M7 Structured Data · **PRIMM focus:** Predict, Run, Investigate, Modify

> **AI today: Rung 3. AI as reviewer.**
>
> | You may | You may not |
> |---|---|
> | Ask AI to explain JSON, an error, or what the checker said. | Ask AI to write your new ending or fix your story file for you. |
> | **After** your story passes the checker, ask AI to critique it. | Use a change you cannot explain. |
>
> "Improvements must be understood and documented (brief note: what changed and why)."

**Goal.** The story leaves the Python and becomes data in a file. You can load it, change it, and check it.

**Files** (in `course-cti110-26fa`):

| File | What it is |
|---|---|
| `p7/toy_story.json` | *The Locked Gate*, a tiny story. The same text as `cyoa_kit/stories/toy.json`. |
| `p7/p7lab2_norris.py` | Opens the story with `json.load` and walks it. Follows `to`, `next` and `ending` only. |
| `cyoa_kit/` | The kit: `game.py` plays any story, `checker.py` checks one, `engine.py` holds the rules. |

---

## Words for today

| Word | Means |
|---|---|
| **JSON** | A text format for data. It looks like Python dicts and lists. It has no comments and no sets. |
| **`json.load(file)`** | Reads a JSON file and gives back Python dicts and lists. |
| **scene** | A place in the story: a `title`, some `beats` (text), maybe `choices`, and one exit. |
| **option** | One answer in a choice group. `to` leaves the scene at once. |
| **`when`** | A condition. In the kit, an option with a false `when` is hidden. |
| **checker** | A program that reads your story and finds problems before a player does. |

The full format is in `cyoa_kit/STORY-FORMAT.md` in your class repository, sections 1 to 8.

---

## 1. Predict

Open `p7/toy_story.json`. Read it from the top.

1. Which scene does the story start in? Which key tells you?
2. You pick `1`, then `1`. Write the screens you will see, up to the next question.
3. What are the two endings called (their `title`s)?
4. The option `"Lift the stone lid"` has `"when": { "field": "role", "is": "fighter" }`. What do you think that means?

<details><summary>Answers</summary>

1. `gate`. The top-level key `"start"`.
2. The Gate text. "Who are you?": `1` is the Fighter. "What do you do?": `1` is "Take the lamp". Then `The lamp is warm. Someone lit it today.` The gate scene has no more groups, so its `"next"` sends you to The Yard: `Past the gate is a yard with a dark well.` and `Your lamp shows a ladder inside the well.` Then "What do you do at the well?"
3. `Down the Well` and `Home Before Dark`.
4. Show this option only to a Fighter.

</details>

## 2. Run

First the demo:

```
cd p7
python3 p7lab2_norris.py
```

Pick `1`, `1`, then look at the well question.

5. How many options does the demo show at the well? Does the Fighter see "Cast a light down the well"?
6. Finish at "Down the Well". The ending prints **both** the Fighter line and the Wizard line. Why? (Read the comment above `show_beats`.)

Now the kit, on the same story:

```
cd ../cyoa_kit
python3 game.py stories/toy.json
```

Pick `1`, `1` again.

7. How many options does the kit show at the well? What does the kit do that the demo does not?

<details><summary>Answers</summary>

5. Four. Yes: the demo numbers **all** options. It ignores `when` on purpose.
6. The demo keeps no state, so it cannot test a `when`. It shows every beat.
7. Three: climb, lift, and go home. The kit **hides** options whose `when` is false. The Wizard's "Cast a light" is hidden from a Fighter. The ending shows only the Fighter's line.

</details>

## 3. Investigate

8. In `p7lab2_norris.py`, find `find_scene`. It loops over a **list**. Why can't it just write `story["scenes"]["yard"]`?
9. Find where the demo decides between `next` and `ending`.
10. In the kit's `engine.py`, find the function that hides options. What is its name? (Hint: STORY-FORMAT.md section 10.2 lists the engine's functions.)

<details><summary>Answers</summary>

8. `story["scenes"]` is a list, not a dict. A list is indexed by number. So we loop and compare each scene's `"id"`.
9. After the groups: `if "next" in scene:` ... `else: target = scene["ending"]`.
10. `visible(items, state)`. It returns the options (or beats) whose `when` is true. `current_group` uses it too.

</details>

## 4. Modify (in the kit)

Run the checker on the toy story first:

```
cd cyoa_kit
python3 game.py stories/toy.json
python3 checker.py stories/toy.json
```

11. What is the checker's last line? Are there warnings? What are they about?

<details><summary>Answer</summary>

11. `RESULT: PASS (0 problems, N warnings)`. The warnings are about size (rule 20): the toy story is smaller than a final project must be.

</details>

**Do not change `stories/toy.json`.** The kit's tests use it. Work on a copy. Put the copy in the kit folder, **not** in `stories/`:

```
cp stories/toy.json my_toy.json
```

Now open `my_toy.json`. Change its first line from `"id": "toy",` to `"id": "my_toy",`. Do this before anything else. Here is why:

- The kit's tests check every story in `stories/` against a saved answer named for the story's id. A practice story there makes the tests fail. That is why the copy stays outside `stories/`.
- The save file is named for the id (`save_toy.json`). Two stories with one id would share one save file.

Every story needs its own id. Yours will too in the final.

12. **Add a third ending.** In `my_toy.json`, add an option to the well group, for example:

    ```json
    { "key": "shout", "label": "Shout down the well", "to": "echo" }
    ```

    Then add the ending to `"endings"`:

    ```json
    "echo": {
      "title": "Only an Echo",
      "beats": [ { "text": "Your voice comes back to you. Nothing else does." } ]
    }
    ```

    Watch the commas: every item in a list or object needs a comma after it, except the last.
13. Run `python3 checker.py my_toy.json`. How many endings does it report now?
14. **Break it on purpose.** Change `"to": "echo"` to `"to": "ecko"`. Run the checker. Copy its `PROBLEM` line. Which rule number does it cite? Put it back.

### Worksheet: predict what the checker will say

The kit has stories broken on purpose in `tests/broken/`. For each one, **predict first**: which rule breaks, and will the result be PASS or FAIL? Then run it and check.

```
python3 checker.py tests/broken/typo_target.json
```

| File | What is wrong (my guess) | Rule # | PASS or FAIL? | What the checker said |
|---|---|---|---|---|
| `bad_json.json` | | | | |
| `typo_target.json` | | | | |
| `unset_flag.json` | | | | |
| `wrong_value.json` | | | | |
| `extra_key.json` | | | | |
| `unreachable_ending.json` | | | | |
| `nested_condition.json` | | | | |
| `no_lever.json` | | | | |
| `stuck.json` | | | | |

Rules are listed in STORY-FORMAT.md section 11.4. The kit's own answer for each is in `tests/broken/<name>.out`.

<details><summary>Answers (what each file is built to break)</summary>

| File | What is wrong | Rule | Result |
|---|---|---|---|
| `bad_json.json` | Not valid JSON. The checker names the line and column. | 1 | FAIL |
| `typo_target.json` | A `to` names a scene or ending that does not exist. | 6 | FAIL |
| `unset_flag.json` | A condition tests a flag that no effect ever sets. | 10 | FAIL |
| `wrong_value.json` | A condition tests a field value that no `set` writes (like `"wizzard"`). | 10 | FAIL |
| `extra_key.json` | A key the format does not allow (like `"sceens"`). | 2 | FAIL |
| `unreachable_ending.json` | An ending no path can reach. | 15 | FAIL |
| `nested_condition.json` | A condition nested more than one level deep. | 10 | FAIL |
| `no_lever.json` | No `role` field set in the start scene, or no option only one role sees. | 18 | FAIL |
| `stuck.json` | A spot the player can reach but from which no ending can be reached. | 16 | FAIL |

A file may also break a second rule along the way. Trust the `.out` file over this table.

</details>

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Running the demo from the wrong folder | `FileNotFoundError: ... 'toy_story.json'` | `cd p7` first. |
| A comma after the last item: `[ 1, 2, ]` | Bad JSON. The checker names the line and column (rule 1). | Remove the last comma. JSON is stricter than Python. |
| A missing comma between items | Bad JSON (rule 1). | Every item but the last needs a comma after it. |
| Single quotes: `'title'` | Bad JSON (rule 1). | JSON uses double quotes only. |
| A `#` comment in the JSON | Bad JSON (rule 1). | JSON has no comments. Put notes in your blueprint. |
| `story["scenes"]["yard"]` | `TypeError: list indices must be integers or slices, not str` | Scenes are a list. Use `find_scene(story, "yard")`. |
| A typo in a `to` | The checker: `PROBLEM ... 'to' names 'ecko', which is not a scene or an ending. (rule 6)` | Copy ids exactly. |
| Editing `stories/toy.json` | The kit's tests fail. | Edit a copy, `my_toy.json`, in the kit folder. |
| A practice copy left in `stories/` | `run_tests.py`: `FAIL check_toy: ...` or `FAIL check_my_toy: there is no tests/check_my_toy.out` | Move practice stories out of `stories/`. Give every copy its own `"id"`. |

---

## Turn in

- [ ] `my_toy.json` (in the kit folder) with `"id": "my_toy"` and a third ending. The checker says `RESULT: PASS`.
- [ ] One paragraph: what the checker said about your broken file (question 14), and what the rule means in your own words.
- [ ] The worksheet table, filled in.

## Exit check

1. Why does the demo show "Cast a light down the well" to a Fighter, but the kit does not?
2. The checker says `RESULT: FAIL (1 problems, 2 warnings)`. Can a player play this story? Should you hand it in?
3. Name two things that are allowed in Python but are bad JSON.
