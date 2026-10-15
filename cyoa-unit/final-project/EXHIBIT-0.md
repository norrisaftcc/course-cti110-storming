# Exhibit 0: A Prompt Chain With No Plan

CTI 110 final project, launch day (Thu 11/19/26). Read the chain below. Then answer the worksheet.

This chain is **made up for this class**. It is written the way many of us talk to a chatbot the first time. Read it as evidence, not as a model. It has wishes. It does not have a plan.

Do not laugh at it. Most of us start this way.

---

## The chain

### Prompt 1 (the first prompt)

> Make me a fantasy text adventure in Python. The player picks a class: warrior, mage or rogue. There should be a dungeon with lots of rooms, monsters, treasure and a dragon at the end. Make it fun and replayable.

### Prompt 2

> This is awesome! Now add a save system so I can quit and keep playing later. Also add an inventory and gold.

### Prompt 3

> Make it spookier. Add a haunted crypt, fog, whispers, and a Sanity meter that goes down when scary stuff happens. More atmosphere in every room.

### Prompt 4

> Add more endings and more choices. Make the choices really matter. Maybe a secret ending.

### Prompt 5 (the last message)

> Perfect. It's due tomorrow. Clean it up and ship it.

### The results (as the chat summed it up)

> Through a series of focused prompts, we built a rich, atmospheric fantasy adventure with real replay value. Players choose from three distinct classes, explore a sprawling haunted dungeon full of monsters and treasure, and manage a Sanity meter that heightens every moment of dread. A full save system and inventory let players come back at any time. Multiple endings, including a secret one, reward bold choices and careful exploration. The result is a polished, immersive game with a strong identity, ready to share.

---

## Worksheet

Work alone for 5 minutes, then compare with a partner. Write short answers. "It doesn't say" is a fine answer, if it is true.

### Part A. The four questions

For each question, find the answer **in the chain**. Quote the words, or write "It doesn't say."

| # | Question | What the chain says |
|---|---|---|
| 1 | **Who plays it?** Who is the player, and for how long? | |
| 2 | **How will you know one thing works?** Pick one feature. What would you check to prove it works? | |
| 3 | **What limit did it set?** A number of rooms, a time, a size, a rule about what the code may do. | |
| 4 | **What did it decide to leave out?** | |

### Part B. Read the results paragraph again

5. The results say the choices "reward bold choices". Which prompt said what a choice should change? Name one choice the game must have.
6. The results say the Sanity meter "heightens every moment of dread". What does the meter **decide**? Which scene or ending changes when it is low? Can you tell from the chain?
7. Prompt 1 says "lots of rooms". Prompt 5 says "clean it up". How would you know when either one is done?

### Part C. Rewrite the first prompt

Rewrite Prompt 1. Stay with the same idea. Add **three lines**:

1. **Who plays it:** ...
2. **How I will know one thing works:** ...
3. **One thing I will leave out:** ...

Example of the shape (not the answer):

> Make me a short text adventure in Python for one player who has five minutes.
> **Who plays it:** a classmate who has never seen it, in one sitting.
> **How I will know one thing works:** if the player picks the mage, the locked door shows "Cast a spell on the lock", and a warrior never sees that option.
> **One thing I will leave out:** combat round by round. A fight is one choice.

Your rewrite:

```
(write it here)
```

---

<details><summary>For the instructor: what the chain leaves out</summary>

| Question | Answer from the chain |
|---|---|
| Who plays it? | It doesn't say. "Fun and replayable" names no player and no length. |
| How will you know one thing works? | It doesn't say. No feature has a test or a check. "Make the choices really matter" has no way to tell if they do. |
| What limit did it set? | Almost none. "It's due tomorrow" is the only constraint. "Lots of rooms" is the opposite of a limit. |
| What did it leave out? | Nothing. Every prompt adds. No prompt removes. |

The defects this kind of chain tends to produce, which the deck shows on slide 4:

- **A meter that decides nothing.** The Sanity meter goes up and down on the screen. No scene or ending reads it.
- **An ending you can jump to.** The save file is plain text. Change the room name in it to the dragon's lair, load, and you win.
- **A half decision.** "Take the amulet" opens a secret ending. "Leave it" changes nothing at all: the game plays exactly as if the player never saw the amulet.

None of these crash. The game plays. Nobody asked the question that would have caught them.

Source of the shape: a measured case study listed in `../SOURCES.md` (the sand castle rows). No text of that case study is reused here.

</details>
