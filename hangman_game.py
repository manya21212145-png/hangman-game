import random

word_categories = {
    "technology": ["python", "github", "algorithm", "function", 
                   "variable", "terminal", "network", "operator"],
    "animals":    ["elephant", "giraffe", "penguin", "dolphin",
                   "crocodile", "butterfly", "cheetah", "kangaroo"],
    "countries":  ["india", "brazil", "canada", "germany",
                   "australia", "argentina", "portugal", "thailand"]
}

HANGMAN_STAGES = [
    """
    -----
    |   |
        |
        |
        |
        |
    ========""",
    """
    -----
    |   |
    O   |
        |
        |
        |
    ========""",
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    ========""",
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
    ========""",
    """
    -----
    |   |
    O   |
   /|\\ |
        |
        |
    ========""",
    """
    -----
    |   |
    O   |
   /|\\ |
   /    |
        |
    ========""",
    """
    -----
    |   |
    O   |
   /|\\ |
   / \\ |
        |
    ========"""
]

def choose_word(category):
    return random.choice(word_categories[category])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    print("\nChoose a category:")
    categories = list(word_categories.keys())
    for i, cat in enumerate(categories):
        print(f"  {i+1}. {cat}")

    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice in ["1", "2", "3"]:
            category = categories[int(choice) - 1]
            break
        print("Invalid choice, try again.")

    word = choose_word(category)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print(f"\nCategory: {category.upper()}")
    print("You have 6 wrong guesses. Good luck!\n")

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word(word, guessed_letters):
            print(f"\nYOU WIN! The word was '{word}'!")
            return True

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Single letters only please.")
            continue

        if guess in guessed_letters:
            print(f"Already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Yes! '{guess}' is in the word!")
        else:
            print(f"Nope! '{guess}' is not in the word.")
            wrong_guesses += 1

    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\nGAME OVER! The word was '{word}'.")
    return False

def main():
    wins = 0
    losses = 0

    while True:
        result = play_hangman()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\nYour record — Wins: {wins} | Losses: {losses}")
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print(f"\nThanks for playing! Final record: {wins}W / {losses}L")
            break

main()