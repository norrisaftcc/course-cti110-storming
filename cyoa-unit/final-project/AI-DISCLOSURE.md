# AI Disclosure

Copy this file to `cyoa_kit/AI-DISCLOSURE.md` and fill it in. Write it yourself.

**Why this file exists.** Disclosure is normal professional practice, not a confession. Engineers say which tools and libraries they used. Writers credit their editors. Here you say what an AI helped with, so a reader knows which choices were yours. AI help that is within the rules and disclosed never costs you points.

Fill it in as you go, not on the last night. It is much easier with `prompts.md` open beside it.

---

## 1. About me and my project

| | |
|---|---|
| Name | |
| Story title and `id` | |
| Build feature (a to f) | |
| Date of this disclosure | |

## 2. Tools I used

Check every tool you used. Add any that are missing.

- [ ] GitHub Copilot chat
- [ ] GitHub Copilot inline suggestions (the grey text as you type)
- [ ] Claude Code
- [ ] A chatbot in a web browser (name it): ____________
- [ ] Other (name it): ____________
- [ ] **I used no AI.** (Then skip section 4 and write "No prompts." in `prompts.md`.)

## 3. The rung in force

| Phase | Rung | Did I follow it? |
|---|---|---|
| Blueprint (Thu 11/19 to Tue 11/24): `blueprint.md` and `story.json` | No AI | Yes / No. If no, say what happened: |
| Build (Tue 11/24 to Thu 12/3): my feature | Rung 4, AI as collaborator | Yes / No. If no, say what happened: |

My tutor config was set to Rung 4 on (date): ________. When I asked "What rung are you on?" it said: ________.

## 4. What each tool helped with

One row for each file or feature an AI helped with. Number your prompts in `prompts.md` and give the numbers here.

| File or feature | What I asked (prompt numbers) | What I kept | What I changed | What I rejected, and why |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## 5. My prompts

All my prompts, in order, with dates: [`prompts.md`](prompts.md)

## 6. One line I can explain

Pick one line of code an AI helped with. Copy it here. Explain it in your own words, in one or two sentences.

```python

```

---

## Examples

### A good disclosure (one row)

| File or feature | What I asked (prompt numbers) | What I kept | What I changed | What I rejected, and why |
|---|---|---|---|---|
| `game.py`, the `c` key (feature b) | Prompts 3 to 6. I pasted my US-F and asked how to add a key that prints the fields. Then I asked why my first try printed `{'role': 'keeper'}` with the braces. | The function `show_sheet(story, state)` and the `elif answer == "c":` line that calls it. | The AI's version printed flags as a Python list. I changed it to print one flag per line, so it matches my user story. | It also wanted to add the flags to `display_plain.py`. I said no: the display may not decide what the game shows, and my golden runs for the Fort story would all change. |

Why it is good: it names the file and the prompts. It says what stayed and what changed. The "rejected" column shows the student checked the answer against the rules and the user story.

### A weak disclosure (one row)

| File or feature | What I asked (prompt numbers) | What I kept | What I changed | What I rejected, and why |
|---|---|---|---|---|
| The code | Help with the game | Most of it | Some stuff | Nothing |

Why it is weak: a reader cannot tell which file, which prompts, or which choices were yours. "Most of it" with nothing rejected suggests nobody checked the answer. Write one row per file or feature, and be specific.
