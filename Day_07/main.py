"""Play a beginner-friendly command-line Hangman game."""

import random

WORD_LIST: tuple[str, ...] = (
    "apple",
    "banana",
    "orange",
    "grape",
    "melon",
    "peach",
    "pear",
    "kiwi",
    "strawberry",
    "blueberry",
)
STARTING_LIVES = 6
HANGMAN_STAGES: tuple[str, ...] = (
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =======
    """,
)


def choose_word(words: tuple[str, ...] = WORD_LIST) -> str:
    """Return a random word from the supplied word list.

    Args:
        words: Available words to choose from.

    Returns:
        A randomly selected word.

    Raises:
        ValueError: If the word list is empty.
    """
    if not words:
        raise ValueError("The word list cannot be empty.")
    return random.choice(words)


def display_word(word: str, guessed_letters: set[str]) -> str:
    """Show guessed letters and underscores for letters still hidden.

    Args:
        word: The word being guessed.
        guessed_letters: Letters already entered by the player.

    Returns:
        The current word display with spaces between characters.
    """
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def display_hangman(lives: int) -> str:
    """Return the non-graphic gallows artwork for the current lives.

    Args:
        lives: Number of remaining incorrect guesses.

    Returns:
        The matching Hangman artwork.

    Raises:
        ValueError: If lives is outside the supported range.
    """
    if not 0 <= lives <= STARTING_LIVES:
        raise ValueError("Lives must be between zero and the starting lives.")
    return HANGMAN_STAGES[STARTING_LIVES - lives]


def get_guess(guessed_letters: set[str]) -> str:
    """Read and validate one new alphabetic guess from the player.

    Args:
        guessed_letters: Letters already entered by the player.

    Returns:
        A lowercase letter that has not been guessed before.

    Raises:
        ValueError: If the player enters anything other than one new letter.
    """
    guess = input("Guess a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        raise ValueError("Please enter one letter.")
    if guess in guessed_letters:
        raise ValueError("You already guessed that letter.")
    return guess


def play_game() -> None:
    """Run one complete Hangman game from start to finish."""
    chosen_word = choose_word()
    guessed_letters: set[str] = set()
    lives = STARTING_LIVES

    print("Welcome to Hangman!")
    print(f"You have {STARTING_LIVES} lives to guess the word.")

    while lives > 0:
        print(display_hangman(lives))
        current_display = display_word(chosen_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Lives left: {lives}")

        try:
            guess = get_guess(guessed_letters)
        except ValueError as error:
            print(error)
            continue

        guessed_letters.add(guess)
        if guess not in chosen_word:
            lives -= 1
            print(f"'{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        if "_" not in display_word(chosen_word, guessed_letters):
            print(f"\nYou win! The word was '{chosen_word}'.")
            return

    print(display_hangman(lives))
    print(f"\nYou lose! The word was '{chosen_word}'.")


def main() -> None:
    """Start the game after confirming that the player is ready."""
    try:
        ready = input("Are you ready to play? (y/n): ").strip().lower()
        if ready != "y":
            print("Game cancelled. Maybe next time!")
            return
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended. Thanks for playing!")


if __name__ == "__main__":
    main()
