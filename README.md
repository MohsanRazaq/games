````markdown
# Hangman Game in Python

A fully interactive terminal-based Hangman game built in Python.  
This project demonstrates core programming concepts including loops, functions, input validation, state management, modular design, and string processing.

Designed as a beginner-to-intermediate Python project while following structured software engineering practices.

---

# Features

- Random word selection
- Interactive terminal gameplay
- Input validation
- Duplicate guess handling
- Warning system
- Vowel/consonant penalty rules
- Dynamic word rendering
- Available letters tracking
- Score calculation
- Hint system (`*` support)
- Modular helper functions
- Clean and readable architecture

---

# Project Structure

.
├── hangman.py
├── words.txt
└── README.md

---

# Requirements

- Python 3.x

No external libraries are required.

Uses only Python standard library modules:
- `random`
- `string`

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hangman-python.git
````

Move into the project directory:

```bash
cd hangman-python
```

---

# Running the Game

Run the main file:

```bash
python hangman.py
```

---

# Gameplay Example

```text
Loading word list from file...
55900 words loaded.

Welcome to the game Hangman!
I am thinking of a word that is 5 letters long.
You have 3 warnings left.
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz

Please guess a letter: a

Good guess: _ a_ _
-------------
```

---

# Game Rules

## Correct Guess

* Reveals matching letters in the word
* No guesses are lost

## Wrong Consonant

* Loses 1 guess

## Wrong Vowel

* Loses 2 guesses

## Invalid Input

Examples:

* numbers
* symbols
* multiple letters

Penalty:

* loses 1 warning
* if warnings reach 0 → loses 1 guess

## Duplicate Guess

* repeated letters trigger warning/guess penalty

---

# Hint System

Players can enter:

```text
*
```

to display possible matching words.

Example:

```text
Possible word matches are:
apple angle amble
```

---

# Helper Functions

## `is_word_guessed()`

Checks whether all letters in the secret word have been guessed.

## `get_guessed_word()`

Displays guessed letters and hidden underscores.

Example:

```text
a _ _ l e
```

## `get_available_letters()`

Shows letters that have not been guessed yet.

## `match_with_gaps()`

Used by the hint system to compare partial words.

## `show_possible_matches()`

Displays matching dictionary words for hints.

---

# Concepts Demonstrated

This project demonstrates:

* loops
* conditional logic
* functions
* string manipulation
* list operations
* modular programming
* input sanitization
* state management
* game architecture
* file handling
* helper-function decomposition

---

# Learning Outcomes

While building this project, the following programming concepts were practiced:

* computational thinking
* breaking problems into smaller components
* debugging logic errors
* validation flow design
* reusable function design
* interactive CLI application structure

---

# Future Improvements

Possible future upgrades:

* difficulty levels
* multiplayer mode
* graphical interface (Tkinter/Pygame)
* leaderboard system
* colored terminal output
* object-oriented refactor
* web version using Flask/Django

---

# Technologies Used

* Python 3
* Standard Library

---

# Author

Mohsan Razaq

---

# License

This project is open-source and available for educational purposes.

```
```
