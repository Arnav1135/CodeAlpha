import random

def get_secret_word():
    words = [
        "python", "jazz", "hangman", "universe", "astronomy", "planet", 
        "galaxy", "computer", "algorithm", "mystery", "elephant", "keyboard", 
        "rhythm", "dinosaur", "giraffe", "adventure", "xylophone", "programming", 
        "bicycle", "ocean", "chocolate", "imagination", "butterfly", "rainbow", 
        "mountain", "volcano", "internet", "discovery", "astronaut", "eclipse", 
        "paradox", "quicksilver", "lightning", "artificial", "encryption", "nebula", 
        "quarantine", "treasure", "vortex", "whirlwind", "zephyr"
    ]
    secret_word = words[random.randint(0, len(words) - 1)]
    return secret_word

def print_guessed_string_with_blanks(secret_word, guessed_string):
    current_guess = list(secret_word)
    i = 0
    for letter in secret_word:
        if letter in guessed_string:
            print(letter, end="")
            current_guess[i] = letter
        else:
            print("_", end="")
            current_guess[i] = "_"
        i += 1
    print()
    return ''.join(current_guess)

def main():
    print("Welcome to Hangman!")
    secret_word = get_secret_word()
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("Guess one character at a time.")
    guesses_left = 6
    guessed_string = ""
    current_processed_guess = ""
    while guesses_left > 0:
        guess = input()
        guessed_string += guess
        if guess in secret_word:
            print("Good guess: " + guess)
            current_processed_guess = print_guessed_string_with_blanks(secret_word, guessed_string)
        else:
            print("Oops! That letter is not in my word: " + guess)
            guesses_left -= 1
            #guessed_string = ""
            #current_processed_guess = ""

        if guesses_left == 0:
            print("You lost! The secret word was: " + secret_word)
            break

        if current_processed_guess == secret_word:
            print("Congratulations! You won!")
            break

main()