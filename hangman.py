import random
import topics_file


def choose_topic():
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


def hangman():
    max_attempts = 6
    while True:
        chosen_word = random.choice(choose_topic())
        display = []
        attempts = max_attempts
        for i in range(len(chosen_word)):
            display += '_'
        print(display)
        game_over = False
        while not game_over:
            guessed_letter = input("Guess a letter: ").lower()
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guessed_letter:
                    display[position] = guessed_letter
            print(display)
            print(f"Attempts left: {attempts}")
            if guessed_letter not in chosen_word:
                attempts -= 1
                if attempts == 0:
                    game_over = True
                    print("Sorry! You've run out of attempts!")
                    print("The correct word was", chosen_word)
            if '_' not in display:
                game_over = True
                print("Congrats! You won!")
        play_again = input("Do you want to play again? (yes/no):\n").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        else:
            print("Starting a new game...\n")


if __name__ == "__main__":
    hangman()
