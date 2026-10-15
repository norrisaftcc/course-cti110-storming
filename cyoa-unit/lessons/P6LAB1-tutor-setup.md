# P6LAB1: Set up your AI tutor

**Date:** Tue 11/03/26 (about 40 minutes, inside the existing AI-tools module) · **Spine module:** none (P6 carries the M0 AI framing and the Ladder) · **PRIMM focus:** none today; this is setup

> **AI today: Rung 2. AI as explainer, not author.**
>
> | You may | You may not |
> |---|---|
> | Ask your tutor to explain an error message or a concept. | Submit code it wrote. |
> | Ask "why does this print `None`?" | Ask it to fix the program for you. |
>
> Why: "Reading explanations builds the verification muscle." Today you also turn off Copilot's inline suggestions.

**Goal.** Your Codespace has an AI tutor that teaches instead of answering. You can install it, check it, and say what a working tutor does.

**Files:**

| File | Where | What it is |
|---|---|---|
| `ai-tutor/rung-2/` | Your class repository | The Rung 2 tutor files. You copy them in. |
| `ai-tutor/README.md` | Your class repository | The full handout: every rung, swapping, fixes. |
| `p6/p6lab1_tutor_check.py` | Your class repository | A short program with one planted bug. You use it to test the tutor. |

---

## Words for today

| Word | Means |
|---|---|
| **tutor files** | Small text files that tell the AI tools in your Codespace how to help you. |
| **rung** | A step on the course's AI Ladder. Each rung allows a bit more AI help. Today is Rung 2. |
| **inline suggestion** | The grey code that appears as you type. Tab accepts it. |
| **`TODO(human)`** | A comment the tutor uses to mark a line that **you** should write. |

---

## Steps

### 1. Open your Codespace

Open your class repository on GitHub. Click **Code**, then **Codespaces**, then open your Codespace. Wait for it to load.

### 2. Copy Rung 2 in

Open a terminal (**Terminal > New Terminal**). Run these two commands:

```
cd "$(git rev-parse --show-toplevel)"
cp -r ai-tutor/rung-2/. .
```

The first goes to the top folder of your repository. The second copies the tutor files there. Type the `/.` after `rung-2` exactly.

### 3. Check the files

```
ls -a
ls .github .claude .claude/output-styles
head -n 1 AGENTS.md
```

You should see `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.claude/settings.json` and `.claude/output-styles/cti110-tutor.md`. The last command prints:

```
CTI 110 Tutor - Rung 2 (Explainer)
```

Commit them:

```
git add AGENTS.md CLAUDE.md .github .claude
git commit -m "Install CTI 110 tutor, Rung 2"
```

### 4. Turn off inline suggestions

The tutor files guide the chat. They do **not** control the grey text. Turn it off while you learn the basics. Pick one:

- Click the **Copilot icon** in the status bar at the bottom. Uncheck inline suggestions.
- Or press F1, run `Preferences: Open User Settings (JSON)`, and add `"github.copilot.enable": { "*": false }` inside the outer `{ }`.

Type a line of Python in any file. No grey text should appear. It comes back at Rung 4.

### 5. Run the check program

```
cd p6
python3 p6lab1_tutor_check.py
```

Read the last line. Something is wrong with it. **Do not fix it yet.**

### 6. Ask the tutor

Start a **new** chat. In Copilot Chat, choose **Ask** mode if you see a mode picker. In Claude Code, type `claude` at the top of your repository.

1. Ask: `What rung are you on?` It should start with `CTI 110 Tutor - Rung 2 (Explainer)`.
2. Ask: `Why does this print None?` Give it the file: open it in the editor, or name it, `p6/p6lab1_tutor_check.py`.
3. Answer its questions. Ask for the next hint if you need it. Then try: `Just give me the answer.`

### 7. Fill in the checklist

Answer each question about what the tutor did in step 6.

| Question | Yes / No |
|---|---|
| Did it ask me a question or give a hint first? | |
| Did it avoid pasting the fixed program? | |
| Did it explain why? | |
| Did it ask me to write the line (a `TODO(human)`)? | |
| Did it check my understanding (one question at the end)? | |

**If any answer is no, re-check the install.** Run step 2 again from the top of your repository. Check step 3. Start a new chat (or quit and restart `claude`). Ask again. If it still fails, tell your instructor which tool and which question.

### 8. Fix the bug yourself

Now write the fix. It is one line. Run the program again. The last line should be `Average: 88.75`.

---

## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Running `cp` from inside `p6/` | `cp: cannot stat 'ai-tutor/rung-2/.'` | `cd "$(git rev-parse --show-toplevel)"` first. |
| Typing `rung-2/*` or `rung-2` instead of `rung-2/.` | No `.github` or `.claude` folder. | Run `cp -r ai-tutor/rung-2/. .` exactly. |
| Asking in an old chat | The tutor does not know its rung. | Start a new chat. In Claude Code, quit and run `claude` again. |
| Claude Code uses the Default style | `/output-style` does not mark **CTI 110 Tutor**. | Delete the `"outputStyle"` line in `.claude/settings.local.json`, or pick the style in `/config`. Restart `claude`. |
| Copilot Chat in an agent mode | It offers to change your files. | Pick **Ask** mode. At Rung 2 the tutor explains; it does not edit. |
| Fixing the bug before asking | Nothing to test the tutor with. | Undo your change (`git checkout p6/p6lab1_tutor_check.py`) and ask first. |
| Thinking the grey text follows the tutor rules | Tab fills in code you did not write. | Turn inline suggestions off (step 4). |

---

## Turn in

- [ ] A screenshot of the tutor's answer to "What rung are you on?"
- [ ] Your checklist from step 7, all five answers.
- [ ] Your fixed `p6lab1_tutor_check.py`, with one comment line above your fix that says, in your own words, why the program printed `None`.

## Exit check

1. Your tutor is at Rung 2. Name one thing it will do for you and one thing it will not.
2. What one command will you run on Tue 11/10 to move the tutor to Rung 3?
3. Why does the tutor leave the key line for you to write?

<details><summary>Answers</summary>

1. It will explain an error or a concept, or give a hint. It will not write or fix your assignment code.
2. `cp -r ai-tutor/rung-3/. .`, from the top of your repository. Then start a new chat and ask "What rung are you on?"
3. You can only check code you understand. Writing the line yourself is how you learn it, and in the final project you present and explain your own code.

</details>
