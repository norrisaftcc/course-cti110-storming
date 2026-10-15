# Stretch: Effects in the Console (optional)

This is optional. You can pick it as your build feature, choice (d) or (e) in `ASSIGNMENT.md`. Or you can do it on top of another feature, for a little extra credit (see `RUBRIC.md`).

The game already has three displays. They show the same game. Only the look changes.

| Display | File | What it does |
|---|---|---|
| plain | `display_plain.py` | Plain ASCII text, 72 columns wide. The default. Every test `.out` file is made with it. |
| ansi | `display_ansi.py` | Colour, a typewriter, boxes and meter bars. |
| curses | `display_curses.py` | A full-screen layout. |

---

## 1. Run it

Inside `cyoa_kit/`:

```
python3 game.py stories/story.json --display ansi
python3 game.py stories/story.json --display curses
```

You can also set the display once for your terminal session: `export CYOA_DISPLAY=ansi`.

In the ANSI display, press **Enter** while the typewriter runs to show the rest of the text at once.

### Windows

`curses` is part of Python on macOS, Linux and Codespaces. On Windows it is not. Install it once:

```
pip install windows-curses
```

If `curses` cannot load, the game uses the plain display and prints one line saying why.

---

## 2. Why the effects switch off

The ANSI display turns **every** effect off, and prints exactly what the plain display prints, when any of these is true:

| When | Why |
|---|---|
| Output is not a terminal (for example, piped into a file or into `cat`) | Colour codes are invisible in a terminal, but in a file they are junk characters such as `\033[36m`. The tests pipe the output and compare it with a `.out` file. Junk would break every test. |
| The environment variable `NO_COLOR` is set to anything | A common rule across many programs: some people cannot read colour, or their screen reader reads the codes aloud. They set `NO_COLOR` once, and every program that follows the rule stays plain. |
| `CYOA_EFFECTS=off` | Our own switch, so you can see the plain look in a real terminal: `CYOA_EFFECTS=off python3 game.py stories/story.json --display ansi`. |

The curses display needs a real terminal too. If output is not a terminal, the game uses the plain display.

### Check that it is plain when piped

Run this. Type `q` and press Enter to quit.

```
python3 game.py stories/story.json --display ansi | cat
```

You should see plain text: no colour, no typewriter delay, no box characters. Or check it with a golden run (use the name of one of your own `.in` files):

```
grep -v '^#' tests/story_escaped.in | python3 game.py stories/story.json --seed 1 --echo --display ansi > ansi.txt
grep -v '^#' tests/story_escaped.in | python3 game.py stories/story.json --seed 1 --echo --display plain > plain.txt
diff ansi.txt plain.txt
```

No output from `diff` means they match. `python3 tests/run_tests.py` does this check for every `.in` file.

---

## 3. The display interface

`game.py` imports one display module as `display` and calls only these eleven functions. If you write or change a display, it must have all eleven, with these exact names and parameters. (Copied from `STORY-FORMAT.md`, section 12.)

| Function | Called | Does |
|---|---|---|
| `start(echo)` | once, before play | Set up the screen. `echo` is `True` or `False` (from `--echo`). |
| `stop()` | once, always, in `finally` | Put the terminal back the way it was. |
| `show_title(story)` | at start and after a restart | The `title` and `subtitle`. |
| `show_scene(scene, beats)` | when a scene is entered or reloaded | The scene `title`, its `place`, then `beats` (already filtered). |
| `show_beats(beats)` | after a pick | The `then` beats (already filtered). |
| `show_roll(report)` | after a pick with a roll | One line: dice, faces, bonus, total, `vs`, result. |
| `show_status(story, state)` | before each choice group | Meters with `hud` not `false` (`Exposure 3/6`), and fields that are not empty (`Role: wizard`). Reads the state; never changes it. |
| `show_choices(group, options)` | before each ask | The `ask`, `[plan]` or `[final]`, then the visible options numbered from 1, each with its `sub` under it. |
| `ask(prompt)` | for every answer | Read one line. Return it stripped. Return `"q"` at end of input or on Ctrl+C. If `echo` is on, print the answer after the prompt. |
| `show_message(text)` | errors, "Saved.", help | One short line. |
| `show_ending(ending, beats, state)` | when an ending is reached | The ending `title`, its beats (already filtered), `THE END`, and the trail of scene titles or ids. |

---

## 4. Ideas

Start small. Change one thing, run it, look at it.

| Idea | Where to look in `display_ansi.py` | Tip |
|---|---|---|
| **Colours by speaker.** Each character has a colour. | `COLORS` and `beat_out(beat)`. A beat's speaker id is in `beat["speaker"]`. | Add a small dict from speaker id to an ANSI code, such as `{"maren": "33", "chen": "35"}`. Use a default colour for anyone not in it. |
| **Typewriter speed.** Faster for action, slower for a reveal. | `DELAY` and `type_out(text, role)`. | `DELAY` is seconds per character. `0.02` is the default. Try `0.01` and `0.05`. |
| **Meter bars.** `Exposure ██████░░░░ 3/6`. | `meter_bar(value, low, high)` and `show_status(story, state)`. | Colour the bar red when the meter is near its `max`. |
| **A screen box.** An in-world phone or terminal. | `box(title, lines)`. A beat's `screen` list is drawn with it. | Use it for a note, a sign or a letter in your story. |
| **Letter-spaced ending titles.** `T H E   F L O O D E D   S T A I R`. | `spaced(text)` and `show_ending(ending, beats, state)`. | Pair it with a short pause before `THE END`. |

For curses, look at `style(name)` and `show_status` in `display_curses.py`. A status line at the top of the screen is a good first change.

---

## 5. Rules

| Rule | Why |
|---|---|
| **Never import `engine`.** | A display shows things. It does not decide them. The checker scans `display_*.py` and warns. |
| **Never change the state.** No `state[...] = ...` in a display. | `show_status` reads the state. If a display changed it, the game would play differently with colour on. The checker warns. |
| **Leave `display_plain` output unchanged.** | Every `.out` file is made with it, for every story in the kit. If you change `display_plain.py`, every golden run changes. |
| **When effects are off, call the `display_plain` function.** | That is how the ANSI display prints exactly the plain output when piped. Use that pattern in every function you change. |
| **Unicode only when effects are on.** | Box and bar characters such as `█` and `┌` are fine in a terminal. The plain output stays ASCII. |
| **Run `python3 tests/run_tests.py` after every change.** | It replays every golden run with the ANSI display, piped. It must still print `ALL TESTS PASSED`. |

Effects are a small bonus. The story, the blueprint and your presentation are worth far more. Do the effects last.
