import random

# Predefined words
words = ["python", "apple", "computer", "house", "garden"]

# Random word selection
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect:

    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Win check
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct/Wrong guess
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")

# Lose condition
if incorrect_guesses == max_incorrect:
    print("\n😢 Game Over! The word was:", word)