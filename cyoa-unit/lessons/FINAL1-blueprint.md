# FINAL1: Sand castle or blueprint

**Date:** Thu 11/19/26 · **Spine module:** M8 Programming Miniproject · **PRIMM focus:** Investigate, then Make (design)

> **AI today: none. No AI on the blueprint.**
>
> | You may | You may not |
> |---|---|
> | Ask the instructor, a tutor or a classmate. | Use AI for ideas, user stories, the map or `story.json`. |
> | Read the checker's messages and `STORY-FORMAT.md`. | Ask AI to fix your JSON. Use the checker's message instead. |
>
> Why: the Ladder's Rung 4 says "Problem formulation, spec, and presentation are yours, and are graded heavily." The blueprint is the formulation. It is 35 of the 100 points. Close the AI chat until the gate on Tue 11/24.

**Goal.** You start your final project the way the rest of the course taught: who plays it, how you will know it works, and what you leave out. By the end of class you have user stories, the start of a map, and a `story.json` the checker has run on.

**Files:**

| File | Where | What it is |
|---|---|---|
| `sandcastle-or-blueprint.html` | `cyoa-unit/deck/` | The launch deck (15 minutes). |
| `EXHIBIT-0.md` | `cyoa-unit/final-project/` | A prompt chain with no plan, and a worksheet. |
| `ASSIGNMENT.md`, `BLUEPRINT-TEMPLATE.md` | `cyoa-unit/final-project/` | The assignment and the blueprint template. |
| `fort_blueprint.md`, `dead_drop_blueprint.md` | `course-cti110-26fa/cyoa_kit/stories/` | Two worked blueprints, with their stories `fort.json` and `dead_drop.json`. |

---

## Words for today

| Word | Means |
|---|---|
| **sand castle** | A build made by stacking prompt on prompt, with no plan. Each wave adds. Nothing decides what to keep. |
| **spike** | A quick build that answers one question. Then you throw it away, or design from what it taught you. |
| **blueprint** | The design you write before you build: user stories, a map, the story file, a cut list. |
| **user story** | "As a player, I want ..., so that ...". One thing a player needs. |
| **Given/When/Then** | A test written in words. Given a start, when the player does this, then this happens. |
| **check** | The proof that a story holds: a checker line, or a golden run. |
| **cut list** | What you left out, why, and when you would bring it back. |
| **lever** | An early choice about who the hero is, stored in the field `role`, that later scenes test. |

---

## 1. The deck (15 minutes)

Watch *Sand Castle or Blueprint*. Write down one sentence from it that you want to remember.

## 2. Exhibit 0 (10 minutes)

Open `EXHIBIT-0.md`. Read the five prompts and the results paragraph. Fill in Part A, the four questions, alone. Then compare with a partner. Then do Part C: rewrite the first prompt with three lines.

1. Which of the four questions does the chain answer best? Which does it not answer at all?

<details><summary>Answer</summary>

1. Only the limit, a little: "It's due tomorrow." It never says who plays it, how to know one thing works, or what to leave out. Every prompt adds; none removes.

</details>

## 3. Investigate: two worked blueprints (15 minutes)

Open `cyoa_kit/stories/fort_blueprint.md`. Open `stories/fort.json` beside it. Then run, inside `cyoa_kit`:

```
python3 checker.py stories/fort.json
```

2. Section 2, the lever. Name one option only the Fighter sees, and one only the Wizard sees.
3. Section 3, US-1. What is its check? Find that exact line in the checker's output.
4. Section 4, the map. Find the edge labelled `(flag oil)`. Which option sets the flag `oil`? (Use section 7.)
5. The checker says `OK real decision: scene 'docks', group 'role'`. Why is choosing the hero a real decision in this story? (Look at the `OK role ... reaches:` lines.)
6. Section 8, the cut list. Pick one row. Do you agree with the reason? What would you cut in your own story?

Now open `dead_drop_blueprint.md`.

7. The Dead Drop lever does two things when you choose. What are they?
8. The `phone` scene has a `route`. Which ending is the default, the one labelled `otherwise`?

<details><summary>Answers</summary>

2. Fighter: "Put your shoulder to the door" (`cellar` / `door` / `shoulder`) and "Hold the doorway and fight" (`store` / `rats` / `fight`). Wizard: "Force the door" (`cellar` / `door` / `force`), "Speak the word of Sleep" and "Fight with your dagger" (`store` / `rats` / `sleep` and `dagger`).
3. `OK lever: scene 'docks' sets role to fighter or wizard.` and the golden run `tests/fort_fighter_win.out`.
4. "Take the tin of lamp oil" in the cottage: `cottage` / `look` / `oil`.
5. The Fighter can reach `flooded_stair` and `rowed_home`. The Wizard can also reach `fell`. The two options lead to different sets of endings. That is what "real decision" means.
6. Your opinion. A good answer names the row and says why.
7. It sets `role` (`enforcer` or `hacker`), and it adds 3 to a stat meter (`body` or `code`) that the dice roll reads later.
8. `noticed` ("A Name on the Frame").

</details>

## 4. Make: your own blueprint (the rest of class, then homework)

Copy the template first. Open `BLUEPRINT-TEMPLATE.md` from the final-project packet, and paste all of it into a new file in your kit: `cyoa_kit/stories/blueprint.md`. Leave every heading as it is.

Work in this order. Do not skip ahead to the JSON.

| Step | What you do | Done when |
|---|---|---|
| a. The pitch | Section 1. One sentence: who plays it, what they do, how long. | A classmate can say it back to you. |
| b. The lever | Section 2. Two values for `role`, and what each one opens. | Each value has at least one option the other never sees. |
| c. User stories | Section 3. 3 to 6 stories. Given/When/Then for each. Leave "Check:" blank for now if you must. | At least one story is about the lever. |
| d. The map | Section 4. Boxes for scenes, rounded boxes for endings, an edge for every exit. | It has 6 to 15 scenes and at least 3 endings. |
| e. `story.json` | Copy `stories/toy.json` to `stories/story.json` and grow it to match your map. Change the `id` to your own. | The JSON matches the map. |
| f. Check it | `python3 checker.py stories/story.json` | The last line is `RESULT: PASS (0 problems, N warnings)`. |

When the checker passes, fill in the "Check:" lines. Use the checker's lines (`OK lever: ...`, `OK role ... reaches: ...`) and the golden runs you will record next week (`tests/story_<ending id>.out`).

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Writing the JSON before the map | A story that wanders, and a checker report full of unreachable scenes (rule 14). | Draw the map first. Then type the JSON from it. |
| A "user story" that is a feature list: "The game has a dragon." | No Given/When/Then fits it. | Start with "As a player, I want ...". Say what the player gets. |
| "Then it works" | Nobody can check it. | Name a real option label or ending: "Then I see 'Force the door'." |
| The lever is set in the second scene | `PROBLEM ... (rule 18)` | Set `role` in a choice group of the **start** scene. |
| Both roles see the same options | `PROBLEM ... (rule 18)`: a value has no option only it can see. | Give each value one option with `"when": { "field": "role", "is": "..." }`. |
| A choice where every option leads to the same endings | `PROBLEM ... (rule 17)`: no real decision. | Make one option close a door: an ending the other options can still reach, this one cannot. |
| A label with parentheses, not in quotes, in the map | The map does not draw on GitHub. | `-->|"Lift the lid (fighter)"|`, in double quotes. |
| A comma after the last item in a JSON list | Bad JSON (rule 1), with a line and column. | Remove it. |
| Keeping the id `toy` | `run_tests.py` checks `toy.json` and `story.json` against the same `tests/check_toy.out`, and one of them fails. | Give `story.json` its own `id`. |

---

## Checklist before you leave

- [ ] Part A and Part C of Exhibit 0 are filled in.
- [ ] `stories/blueprint.md` exists, with sections 1, 2 and 3 started.
- [ ] I have a map with at least the start scene, the lever, and 3 endings.
- [ ] I have run the checker on my `story.json` at least once, even if it fails.
- [ ] My AI chat stayed closed.

**Due at the start of class Tue 11/24/26:** `stories/blueprint.md` and `stories/story.json`. The checker must print `RESULT: PASS`.

## Exit check

1. In one sentence: what is the difference between a spike and a sand castle?
2. Write one Given/When/Then for your own lever.
3. Name one thing you will leave out of your story, and why.
