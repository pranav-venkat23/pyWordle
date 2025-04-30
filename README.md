# APCSP Wordle Project - "pyWordle"

A Python-based Wordle game built for my AP Computer Science Principles Create Task. The game selects a random five-letter word from a large `.txt` word list and gives symbol-based feedback after each guess.

## 🔹 How to Play
- You have 6 tries to guess the 5-letter word.
- After each guess:
  - `$` = correct letter and position
  - `%` = correct letter, wrong position
  - `*` = incorrect letter

## 🛠 Features
- Random word selection from a large text file
- Input validation (real word and length check)
- Feedback tracking with letter status updates

## ▶️ How to Run
1. Make sure `words.txt` is in the same folder.
2. Run the game in your terminal:
   ```bash
   python wordle.py
