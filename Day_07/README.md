# 📅 Day 7 -- Hangman Game

## 🚀 Overview
Today, I worked on creating a simple Hangman game using Python. The game allows the user to guess a word by suggesting letters within a certain number of attempts. It was a fun way to practice my coding skills and apply concepts like loops, functions, and conditional statements.


## 📚 Concepts covered in this project
- Loops (for and while)
- Functions
- Conditional statements (if, elif, else)
- String manipulation
- Python lists
- Random module for selecting a word

## 🎮 Hangman Game

## 🛠 How It Works
1. The game starts by selecting a random word from a predefined list of words.
2. The user is prompted to guess a letter.
3. The program checks if the guessed letter is in the word and updates the display accordingly.
4. The user has a limited number of attempts to guess the word correctly.
5. The game ends when the user either guesses the word correctly or runs out of attempts.

## 💻 Run the game

From the repository root, run:

```bash
python Day_07/main.py
```

The game chooses a word from a small fruit-themed word list. Enter one
alphabetic letter per turn. Repeated guesses and invalid input do not cost a
life, while incorrect guesses reduce the six available lives.

## 💻 Code
### [View Code](main.py)

## 🧠 What I Learned
- How to use loops and functions to structure the code effectively
- How to manipulate strings and lists to keep track of the user's guesses and the current state of the word
- How to use the random module to select a word from a list
- How to implement game logic and manage user input in a fun and interactive way
- How to use sets for efficient duplicate-guess checks
- How to organize a command-line program with functions and a `main()` entry point

## ⚡ Challenges Faced
- Designing the game logic to handle user input and update the game state correctly
- Ensuring that the game provides clear feedback to the user about their guesses and remaining attempts

## 🔥 Future Improvements
- Add a graphical interface (GUI) to enhance the user experience
- Implement a scoring system based on the number of attempts taken to guess the word
- Allow the user to choose different difficulty levels with varying word lengths and number of attempts