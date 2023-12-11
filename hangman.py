import random
import topics_file
import hangman_drawings

def choose_topic_menu():
    """
    Lets the user choose a topic for the Hangman game.
    
    Returns:
        list: A list of words based on the chosen topic.

    >>> topics_file.colors
    ['blue', 'green', 'yellow', 'purple', 'red', 'orange', 'violet', 'pink', 'black', 'white']
    >>> topics_file.animals
    ['dog', 'cat', 'horse', 'turtle', 'elephant', 'tiger', 'hippopotamus', 'cheetah', 'panda', 'giraffe']
    >>> topics_file.countries
    ['unitedstates', 'mexico', 'canada', 'india', 'china', 'nepal', 'japan', 'australia', 'france', 'finland', 'zimbabwe', 'denmark', 'chile', 'dominicanrepublic', 'ethiopia', 'jamaica', 'honduras']
    """
    while True:
        print("Welcome to hangman! Choose a topic to start playing:")
        print("1. Colors")
        print("2. Animals")
        print("3. Countries")
        choice = input("Enter topic number: ")
        if choice == '1':
            return topics_file.colors
        elif choice == '2':
            return topics_file.animals
        elif choice == '3':
            return topics_file.countries
        else:
            print("Invalid choice. Please try again.")

def initialize_game():
    """
    Initializes a new hangman game.

    Returns:
        tuple: A tuple containing the chosen word, display list, and attempts count.
    """
    max_attempts = 6
    chosen_word = random.choice(choose_topic_menu())
    display = ['_' for _ in range(len(chosen_word))]
    attempts = max_attempts
    return chosen_word, display, attempts

def display_current_state(display, attempts):
    """
    Displays the current state of the game, including the word display, remaining attempts, and the hangman drawing.

    Parameters:
        display (list): The current display list of the guessed word.
        attempts (int): The number of attempts remaining.
    """
    print("Current Word:", " ".join(display))
    print(f"Attempts left: {attempts}")
    print(hangman_drawings.drawings[attempts])

def get_valid_guess(guessed_letters):
    """
    Prompts the user to guess a letter and ensures the input is a valid single letter that hasn't been guessed before.

    Parameters:
        guessed_letters (set): A set of letters already guessed.

    Returns:
        str: A valid letter guessed by the user.
    """
    while True:
        guessed_letter = input("Guess a letter: ").lower()
        if guessed_letter.isalpha() and len(guessed_letter) == 1 and guessed_letter not in guessed_letters:
            return guessed_letter
        else:
            print("Invalid input. Please enter a valid single letter that you haven't guessed before.")

def update_display(chosen_word, display, guessed_letter):
    """
    Update the display list with the guessed letter.

    Args:
        chosen_word (str): The word to guess.
        display (list): The current display list.
        guessed_letter (str): The guessed letter.

    >>> update_display('hangman', ['_', '_', '_', '_', '_', '_', '_'], 'a')
    ['_', 'a', '_', '_', '_', 'a', '_']
    """
    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter:
            display[position] = guessed_letter
    return display

def play_hangman():
    max_attempts = 6

    while True:
        chosen_word, display, attempts = initialize_game()
        guessed_letters = set()
        game_over = False

        while not game_over:
            display_current_state(display, attempts)
            guessed_letter = get_valid_guess(guessed_letters)
            guessed_letters.add(guessed_letter)

            if guessed_letter in chosen_word:
                update_display(chosen_word, display, guessed_letter)
            else:
                attempts -= 1

            if attempts == 0 or '_' not in display:
                game_over = True

        play_again = input("Do you want to play again? (yes/no):\n").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        else:
            print("Starting a new game...\n")

#if __name__ == "__main__":
    #import doctest
    #doctest.testmod(verbose=True)
play_hangman()
