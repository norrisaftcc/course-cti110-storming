# P7BONUS: Endings in a database (optional)

**Date:** Tue 11/17/26 (optional, after P7LAB3) · **Spine module:** M7 Structured Data (the sqlite3 recap) · **PRIMM focus:** Predict, Run, Modify

> **AI today: Rung 3. AI as reviewer.**
>
> | You may | You may not |
> |---|---|
> | **After** your code works, ask AI to critique it. Ask it to explain SQL words you do not know. | Ask AI to write your functions or your SQL. |
>
> "Improvements must be understood and documented (brief note: what changed and why)."

**Goal.** You can store rows in a sqlite3 table and ask the table a question: how many endings has the player found?

**Demo file** (in `course-cti110-26fa`): `p7/p7bonus_sqlite_norris.py`. It makes `endings.db` and prints `Endings found: 2 of 3`.

---

## Words for today

| Word | Means |
|---|---|
| **database** | Data kept in tables, with a language (SQL) to ask questions about it. |
| **sqlite3** | A small database that comes with Python. The whole database is one file. |
| **table** | Rows and columns. Our table `endings` has two columns: `story` and `ending`. |
| **`UNIQUE(story, ending)`** | The same pair can never be stored twice. |
| **`INSERT OR IGNORE`** | Add a row; if it would break `UNIQUE`, skip it quietly. |
| **`?`** | A placeholder. sqlite3 fills it in safely from a tuple. |
| **`commit()`** | Save the changes to the file. |

---

## 1. Predict

Read `p7/p7bonus_sqlite_norris.py`.

1. `main()` adds three rows. How many are stored? Why?
2. What does the program print?
3. You run it a **second** time. What does it print now?

<details><summary>Answers</summary>

1. Two. `flooded_stair` is added twice. `UNIQUE` plus `INSERT OR IGNORE` keeps only one.
2. `Endings found: 2 of 3`
3. `Endings found: 2 of 3` again. The file keeps the rows from the first run, and the repeats are ignored.

</details>

## 2. Run

```
cd p7
python3 p7bonus_sqlite_norris.py
python3 p7bonus_sqlite_norris.py
```

4. Was your answer to question 3 right? Look in the folder: what new file is there?

## 3. Investigate

5. Why does `count_endings` write `(story,)` with a comma?
6. Why use `?` instead of putting the text into the SQL with an f-string?
7. Delete `INSERT OR IGNORE` and write `INSERT` instead. Delete `endings.db`. Run. What happens? Put it back.

<details><summary>Answers</summary>

5. `(story,)` is a tuple with one item. `(story)` is just the string. sqlite3 would treat each **letter** as a value: `Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.`
6. A name with a quote in it (`Keeper's`) would break the SQL. Worse, typed text could change the SQL. `?` lets sqlite3 fill the value in safely.
7. The second `flooded_stair` breaks the rule: `sqlite3.IntegrityError: UNIQUE constraint failed: endings.story, endings.ending`.

</details>

## 4. Modify

8. Add the third ending, `fell`. Run. What prints?
9. Write `list_endings(conn, story)`. It runs `SELECT ending FROM endings WHERE story = ?` and returns a list of names. Print them under the count.
10. Add a second story, `"dead_drop"`, with its own endings. Does the Fort count change?

## 5. Make (stretch)

11. Make the count tell the player which endings are still missing. (Hint: loop over `all_endings` and test `in` the list from question 9.)

To start over at any time, delete `endings.db`.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Forgetting `conn.commit()` | The rows are gone next run. | Commit after each change. |
| `(story)` instead of `(story,)` | `sqlite3.ProgrammingError: Incorrect number of bindings supplied...` | One-item tuples need the comma. |
| Pasting text into SQL with an f-string | Breaks on a quote. Unsafe. | Use `?` and a tuple. |
| `INSERT` without `OR IGNORE` on a `UNIQUE` table | `sqlite3.IntegrityError: UNIQUE constraint failed` | `INSERT OR IGNORE` |
| Running from another folder | A new, empty `endings.db` appears there. The count is 0. | Run from `p7`. |
| Committing `endings.db` to Git | A binary file in your repository. | Do not `git add` it. |

---

## Turn in (if your instructor makes it required)

- [ ] Your changed file with `list_endings` and the count.
- [ ] Output from two runs, showing the count does not grow on repeats.
- [ ] The two-line Rung 3 review note at the top.

## Exit check

1. What does `UNIQUE(story, ending)` stop from happening?
2. Why is `?` safer than an f-string in SQL?
