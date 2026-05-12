import random
import string

WORDLIST_FILE = "words.txt"

# -----------------------------------
# LOAD WORDS
# -----------------------------------

def load_words():

    print("Loading word list from file...")

    with open(WORDLIST_FILE, 'r') as f:
        line = f.readline()

    wordlist = line.split()

    print(" ", len(wordlist), "words loaded.")

    return wordlist


wordlist = load_words()


# -----------------------------------
# CHOOSE RANDOM WORD
# -----------------------------------

def choose_word(wordlist):

    return random.choice(wordlist)


# -----------------------------------
# CHECK IF WORD GUESSED
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):

    for letter in secret_word:

        if letter not in letters_guessed:
            return False

    return True


# -----------------------------------
# DISPLAY CURRENT WORD
# -----------------------------------

def get_guessed_word(secret_word, letters_guessed):

    guessed_word = ''

    for letter in secret_word:

        if letter in letters_guessed:
            guessed_word += letter + " "

        else:
            guessed_word += "_ "

    return guessed_word


# -----------------------------------
# AVAILABLE LETTERS
# -----------------------------------

def get_available_letters(letters_guessed):

    available_letters = ''

    for letter in string.ascii_lowercase:

        if letter not in letters_guessed:
            available_letters += letter

    return available_letters


# -----------------------------------
# MATCH WITH GAPS
# -----------------------------------

def match_with_gaps(my_word, other_word):

    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):

        if my_word[i] == '_':

            if other_word[i] in my_word:
                return False

        elif my_word[i] != other_word[i]:
            return False

    return True


# -----------------------------------
# SHOW POSSIBLE MATCHES
# -----------------------------------

def show_possible_matches(my_word):

    matches = []

    for word in wordlist:

        if match_with_gaps(my_word, word):
            matches.append(word)

    if len(matches) == 0:
        print("No matches found")

    else:
        print(" ".join(matches))


# -----------------------------------
# MAIN GAME ENGINE
# -----------------------------------

def play_game(secret_word, with_hints=False):

    guesses = 6
    warnings = 3
    vowels = 'aeiou'
    letters_guessed = []

    print("Welcome to the game Hangman!")

    print("I am thinking of a word that is",
          len(secret_word),
          "letters long.")

    print("You have", warnings, "warnings left.")
    print("-------------")

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):

        print("You have", guesses, "guesses left.")

        print("Available letters:",
              get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower().strip()

        # -----------------------------------
        # HINT FEATURE
        # -----------------------------------

        if with_hints and guess == "*":

            print("Possible word matches are:")

            show_possible_matches(
                get_guessed_word(secret_word, letters_guessed)
            )

            print("\n-------------")
            continue

        # -----------------------------------
        # INVALID INPUT
        # -----------------------------------

        if not guess.isalpha() or len(guess) != 1:

            if warnings > 0:

                warnings -= 1

                print("Oops! That is not a valid letter. You have",
                      warnings,
                      "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))

            else:

                guesses -= 1

                print("Oops! That is not a valid letter. "
                      "You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

            print("-------------")
            continue

        # -----------------------------------
        # DUPLICATE LETTER
        # -----------------------------------

        if guess in letters_guessed:

            if warnings > 0:

                warnings -= 1

                print("Oops! You've already guessed that letter. "
                      "You now have",
                      warnings,
                      "warnings:",
                      get_guessed_word(secret_word, letters_guessed))

            else:

                guesses -= 1

                print("Oops! You've already guessed that letter. "
                      "You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

            print("-------------")
            continue

        # -----------------------------------
        # STORE GUESS
        # -----------------------------------

        letters_guessed.append(guess)

        # -----------------------------------
        # CORRECT GUESS
        # -----------------------------------

        if guess in secret_word:

            print("Good guess:",
                  get_guessed_word(secret_word, letters_guessed))

        # -----------------------------------
        # WRONG GUESS
        # -----------------------------------

        else:

            print("Oops! That letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))

            if guess in vowels:
                guesses -= 2

            else:
                guesses -= 1

        print("-------------")

    # -----------------------------------
    # GAME RESULT
    # -----------------------------------

    if is_word_guessed(secret_word, letters_guessed):

        unique_letters = len(set(secret_word))

        score = guesses * unique_letters

        print("Congratulations, you won!")

        print("Your total score for this game is:", score)

    else:

        print("Sorry, you ran out of guesses.")

        print("The word was:", secret_word)


# -----------------------------------
# NORMAL GAME
# -----------------------------------

def hangman(secret_word):

    play_game(secret_word)


# -----------------------------------
# GAME WITH HINTS
# -----------------------------------

def hangman_with_hints(secret_word):

    play_game(secret_word, True)


# -----------------------------------
# RUN PROGRAM
# -----------------------------------

if __name__ == "__main__":

    secret_word = choose_word(wordlist)

    # Normal game
    #hangman(secret_word)


    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)