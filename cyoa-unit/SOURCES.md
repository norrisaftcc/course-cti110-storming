# Sources

Every source this unit borrows from. Read-only for this unit: nothing here was changed in the source repositories.

**Fit** says how much we took. **As-is**: used without change. **Adapt**: rewritten for CTI 110 (no classes, Python 3.10, plain words, the 26fa header). **Idea only**: the idea or the shape, not the text.

## Repositories and commits

| Short name | Repository | Branch | Commit |
|---|---|---|---|
| Fort | `games-osr-fort-on-lake` | `main` | `169ee8f9588adededc309db93f91ca93908a0706` (2026-10-14, merge of PR #7) |
| HTLL PR #34 | `game-high-tech-low-lives` | `claude/stage-dead-drop` | `97a8682db5549146e7a07d3167e1c89b903824d1` |
| HTLL main | `game-high-tech-low-lives` | `main` | `888aa3ee16be6c3ad2d1042770f965e518d068e9` |
| team-ycbbb | `team-ycbbb` | `main` | `defc364eeb107e065b2d8fc4309e36abd92075f2` (Neon Wake last changed at `c74d214`, 2026-10-07) |
| 26fa | `course-cti110-26fa` | `claude/cyoa-unit` | base `b7dc7c7c118389af54b2ad44d728f5c806ea3dd9` |
| storming | `course-cti110-storming` | `claude/cyoa-unit` | base `4fc2cb144f0cbcd2563112e91645999fb9d3330c` |

---

## Fort on the Lake (Fort, main `169ee8f`)

| Path | What we took | Where it went | Fit |
|---|---|---|---|
| `stage/SPEC.md` §2 | Every key name and meaning of the story format: scene `id`/`title`/`place`/`beats`/`choices`/`next`/`ending`/`route`; beat `text`/`speaker`/`when`/`screen`; group `key`/`ask`/`gate`/`options`; option `key`/`label`/`sub`/`when`/`effects`/`then`/`to`/`roll`; conditions; effects; endings; `pack.json` `id`/`title`/`subtitle`/`start`/`resolver`/`meters`/`fields`; the roll's `ose` and `fate4df` reading. | `final-project/STORY-FORMAT.md` | Adapt (a strict subset; see its §13) |
| `stage/SPEC.md` §3 | `validate` and `simulate` as the model for the checker: references resolve, every ending reachable, explore projected states, branch on every roll result the dice can reach. | `cyoa_kit/checker.py` | Idea only |
| `classroom/python/stage3_dungeon_clock.py` | The "same block pasted twice" setup; S1 to C1 room text; the Fighter and Wizard as printed. | `p5/p5lab1_before_norris.py`; `stories/fort.json` | Adapt (no mulberry32, no `global`, no OSE notation) |
| `classroom/python/stage4_dice_functions.py` | One new function shape at a time (`is_yes`, `check`, `attack`, `tick`, `torch_out`); `main()` at the bottom. | `p5/p5lab1_norris.py`, `p5/p5lab2_norris.py` | Adapt (functions return values; the caller prints) |
| `classroom/stages/stage4.md` (mistakes table) | Five Python rows: no parentheses, no `return`, result not saved, printing instead of returning, argument order. | `lessons/P5LAB1-…`, `P5LAB2-…` | Adapt (C++ rows dropped; "main() before the defs" added) |
| `classroom/stages/stage3.md` (mistakes table) | Infinite loop; `turn + 1` not assigned; `== 0` vs `<= 0`. | `lessons/P5LAB1-def-call-main.md` (bridge from loops) | Adapt |
| `classroom/python/stage5_five_rats.py` | Outcome sentences: the Fighter holds the doorway; the Wizard speaks Sleep; the fall among the jars; backing up the stair. | `stories/fort.json` (scene `store`) | Adapt (the fight becomes a choice on `role`) |
| `classroom/python/stage6_rooms_as_data.py` | Room ids, one-line room texts and exits for S1 to C3; the trapdoor under the rubble; "five flasks of oil are still whole". | `stories/fort.json`; `p6/p6lab2_rooms_norris.py`; `p7/p7lab1_norris.py` | Adapt (records become dicts; string ids) |
| `classroom/stages/stage6.md` (mistakes) | Exits that do not go both ways; testing a room by its title instead of its id. | Checker rule 3 and the "use the id" line in `STORY-FORMAT.md` | Idea only |
| `classroom/README.md` | "Send the Fighter to the door"; the Wizard's poor odds at the stuck door. | The Fort lever in `fort_blueprint.md` | Idea only |
| `dm/Module_2_The_Drowned_Tower.md` line 127, lines 624-638 | "Let the Fighter be the one who opens the dungeon"; the stuck oak door at C1; the clever answer "oil the hinges from a flask". | The Fort lever and the `oil` flag in `stories/fort.json` | Idea only (Fort's own text; nothing past C3) |
| `campaign/SPINE.md` line 29 and lines 199-206; `AGENTS.md` | The IP rule; the Module 2 pinned facts for the island; the rules on the lake city and the campaign's secret. | Rules for the Fort example; `instructor/scan_fort_names.py` | As-is (reference) |
| `generator/test.mjs` lines 20-21; `intro/test.mjs` line 49 | The machine-checked forbidden-name patterns. | Read at run time by `instructor/scan_fort_names.py`. Not copied into any file of this unit. | As-is (read at run time) |
| `intro/SPEC.md` | "Choices write onto a card": an early choice stored as a field that later scenes read. | The lever explanation in `STORY-FORMAT.md` §7 and the lessons | Idea only |

**What the Fort example does not take.** Nothing from the 1977 Basic sample dungeon or any other Wizards of the Coast book: no names, room keys, read-aloud, maps or NPCs. Nothing past C3 of Module 2: no grotto, no door under the lake, none of the grotto's people. The drowned city is not keyed. The campaign's secret is not mentioned.

---

## High Tech, Low Lives (HTLL)

### PR #34, `claude/stage-dead-drop` at `97a8682` (read with `git show`)

| Path | What we took | Where it went | Fit |
|---|---|---|---|
| `arcade/stage/packs/dead-drop/script.json` | Scene ids `arrive`, `counter`, `drop`, `table`, `phone`, `abort`; ending ids `clean`, `noticed`, `debrief`, `aborted`; trimmed beats; the groups `observe`, `approach`, `pay`, `pass`; the exposure route in `phone`. | `stories/dead_drop.json` | Adapt (cut from 9 scenes and 7 endings to 6 and 4; `look`, `set`, `kicker`, `notes`, `comment` removed; the Fate economy removed) |
| `arcade/stage/packs/dead-drop/pack.json` | Meters `exposure`, `nerves`, `systems`; fields `identity`, `drop`; resolver `fate4df`; start `arrive`. | `stories/dead_drop.json` header | Adapt (`fate`, `meat`, `chenKnows`, `learned` cut; `body` and `code` added as stat meters; `bad`, `hud` on bad meters, `kit`, `storageKey`, `commentary` not used) |
| `arcade/stage/packs/dead-drop/NOTES.md` | The plan table, endings table and meter table as a model for a design doc; the voice checks; Chen is "she", with no portrait. | `stories/dead_drop_blueprint.md`; `BLUEPRINT-TEMPLATE.md` | Idea only |
| `arcade/stage/packs/dead-drop/notes.json` | The plain-words explanation of plan and exec, and of 4dF. | `STORY-FORMAT.md` §4.3 and §8 | Idea only |

**New for this unit, not HTLL canon:** the lever group `role` in `arrive`; the pass options `muscle` (Enforcer) and `loop` (Hacker); the `cover` group in `table`; the role-gated lines. The blueprint labels them.

### HTLL main at `888aa3e`

| Path | What we took | Where it went | Fit |
|---|---|---|---|
| `build/docs-v2/enforcer_playbook_v2.md` | The Enforcer: Body +3, chrome, "problems solved with presence"; Systems stress when chrome fails. | The `enforcer` side of the Dead Drop lever | Idea only |
| `build/docs-v2/hacker_playbook_v2.md` | The Hacker: Code high, Body +0, the deck and the feed; a Nerves cost. | The `hacker` side of the lever | Idea only (the playbook's Code +4 is set to +3 so the two sides are even) |
| `build/docs-v2/infiltrator_playbook_v2.md` | Ann/Shodann stays the hero, so Chen's lines still fit. | `stories/dead_drop.json` | Idea only |
| `prototype/deck_mvp.py` | Display techniques: a palette by role, a strip-colours switch, the typewriter, box panels, `■`/`□` meter bars, speaker headers, a `[n]` choice menu with an error line, a batch mode for tests. | `cyoa_kit/display_ansi.py`; `STRETCH-EFFECTS.md` | Adapt (no classes; no text copied; the script's language is not reused) |
| `prototype/scene_format.md` | Only the idea that the author marks the speaker and the display picks the colour. | `display_ansi.py` | Idea only (its schema is not used) |
| `.claude/projects/twine-if/story-structure.md` lines 263-280, 368-415 | An early choice that sets a stat; "each option has merit and a cost; don't punish choices". | `STORY-FORMAT.md` §7; `ASSIGNMENT.md` | Idea only |

---

## team-ycbbb (`spooks/neon-wake/`, main `defc364`)

| Path | What we took | Where it went | Fit |
|---|---|---|---|
| `PLAN.md` | Sand castle vs blueprint; "A spike that answers a question and is then thrown away is good practice. The failure is a spike that is promoted without a design pass." | `README.md`; `ASSIGNMENT.md`; the deck | Adapt |
| `00-prompt-transcript.md` | The shape of "Exhibit 0" and its four missing things: user, acceptance criterion, constraint, cut. | `final-project/EXHIBIT-0.md` (new text, a CYOA chain) | Adapt (no text reused) |
| `AUTOPSY.md` §3, §5, §7, §8 | A real decision is "a choice that changes a later outcome"; what the sand castle did better. | Checker rule 17; the deck | Idea only |
| `design/01-stories.md` §4-§7 | User stories with Given/When/Then criteria that name their check; the cut list with "revisit when". | `BLUEPRINT-TEMPLATE.md`; the two worked blueprints | Adapt (no evidence or requirement ids) |
| `design/02-design-brief.md` §2, §3, §5, §8 | The three layers with "owns" and "may not"; the frozen API; D-08 (map the typed number to the option's key); D-10 (flags as a sorted list, so state survives JSON). | `STORY-FORMAT.md` §1, §4.4, §10 | Adapt |
| `game/neon_wake/engine.py` | The API shape (`new_state`, `visible`, `choose` returns a new state, `is_over`) and `validate_story`'s report style: one problem per line, naming the scene and the rule. | `cyoa_kit/engine.py`, `cyoa_kit/checker.py` | Adapt (about half the size; no stat allocation; JSON instead of a Python dict) |
| `game/neon_wake/story.py` | The graph pattern: an early lever, lever-gated bypasses, a flag-gated choice, a refusal ending. | Both worked stories | Idea only (no text) |
| `game/console.py` | The loop shape; injected input; "R restarts, Q quits"; `--echo` for recorded runs. | `cyoa_kit/game.py` | Adapt (no `class _Quit`; a `"q"` answer instead) |
| `game/sample-run.txt` | The golden-run format. | `tests/*.in` and `.out` | Adapt |
| `game/tests/test_bfs.py`, `test_engine.py`, `test_story.py`, `test_console.py` | Explore every path; reach every ending; no dead scene; the JSON round trip; the boundary pair; the broken-story table; a blocklist scan; the display rule-leak check. | `cyoa_kit/checker.py`, `cyoa_kit/tests/` | Adapt (plain functions and `assert`; no `unittest.TestCase`) |
| `sprint-1/definition-of-done.md` | DoD-03 "a rule appears in exactly one place"; DoD-05 someone else ran it. | `ASSIGNMENT.md` (Definition of Done) | Idea only |
| `slides.html` | The deck engine and the two visual registers; 11 of 18 slides, rewritten for CTI 110. | `deck/sandcastle-or-blueprint.html` | Adapt (team and CTS-285 material removed) |
| `README.md` | The "Use it" table and the honesty section. | This unit's `README.md` | Adapt |

Not taken: any Neon Wake or sand-castle story text; the sand castle's company name.

---

## CTI 110 (this course)

| Path | What we took | Fit |
|---|---|---|
| storming `cti110-refresh-planning/CTI-110-course-spine.md` | Module numbers (M6 functions, M7 structured data, M8 miniproject); PRIMM; the SDLC arc; front-loaded formulation; the presentation as the audit; 10th-grade prompts; Mermaid. | As-is (reference) |
| storming `cti110-refresh-planning/CTI-110-ai-assistance-ladder.md` | Rungs 2, 3 and 4; disclosure from Rung 3; Copilot norms and settings. | As-is (reference) |
| 26fa `p3/M3BONUS_norris.py` | Each door is a function; the seed for the room-calls-room trap. | Idea only |
| 26fa `p3lab_norris.py` | The making-change lab, refactored in P5LAB3. | Adapt |
| 26fa `p4/p4lab2_norris.py`, `p3/p3t1_norris.py` | The file header, section comments, `main()` at the bottom with its comment. | As-is (style) |
| 26fa `p2/p2lab2_norris.py`, `p2/p2hw2_setup.py` | Students' first dicts and lists; the P7 refresher points back to them. | As-is (reference) |
| 26fa `_practice/practice.py` | Stub functions with `pass`. | Idea only |
