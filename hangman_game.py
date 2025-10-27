# HANGMAN GAME

from wordlist import words
import random
import time


hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}


###############################################################################################################


def main_menu():

    print('******************************************************************')
    print('**                                                              **')
    print('**            WELCOME TO HANGMAN GAME                           **')
    print('**                                                              **')
    print('**     1. Start game (press "s")                                **')
    print('**     2. Exit game (press "e")                                 **')
    print('**     3. Feedback and review (press f)                         **')
    print('**    --> All types of words included (🐒,🏴,🐥,🚕,📷,etc..)    **')
    print('**                                                              **')                                               
    print('******************************************************************')
    
###############################################################################################################

def display_man(wrong_guesses):

    print('\n******************************')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print('******************************')


###############################################################################################################


def display_hint(hint):
    print(" ".join(hint))


###############################################################################################################


def display_answer(answer):
    print(" ".join(answer))


###############################################################################################################


def main():
    while True:  # Game keeps running until user exits
        main_menu()
        choice = input("Enter your choice (s/e/f): ").lower()

        if choice == 's':
            answer = random.choice(words)
            hint = ["_"] * len(answer)
            wrong_guesses = 0
            guessed_letters = set()
            is_running = True

            while is_running:
                display_man(wrong_guesses)
                display_hint(hint)
                guess = input("\nEnter a letter: ").lower()

                if len(guess) != 1:
                    print("Invalid input 🤔. Guess one letter at a time.")
                    continue
                elif not guess.isalpha():
                    print("Invalid input 🤔. Guess a letter.")
                    continue

                if guess in guessed_letters:
                    print(f'{guess} is already guessed.')
                    continue

                guessed_letters.add(guess)

                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess
                else:
                    wrong_guesses += 1

                if '_' not in hint:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print('Congratulations! You win 🎉')
                    is_running = False
                elif wrong_guesses >= len(hangman_art) - 1:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print(f'You lose! Better luck next time 😞')
                    is_running = False

            # After one game ends
            play_again = input("\nDo you want to play again (y/n)? : ").lower()
            if play_again != 'y':
                print("Thanks for playing! Goodbye 🙋")
                break  # Exit the loop, end the program

        elif choice == 'e':
            print("Thanks for visiting, byee 👋")
            break  # Exit the loop completely

        elif choice == 'f':
            print("\nRedirecting to feedback and review section")
            for i in range(3):
                print("Loading" + "." * (i + 1))
                time.sleep(0.5)
            print()
            rating = float(input("How much do you rate us out of 5? : "))
            provide = input("Please provide feedback for improvements:\n")
            print()
            print(f'''We appreciate your rating 👍 {rating}/5 
Thanks for the feedback — we'll work on it ✅''')
            print('Byee! 👋')
            break  # Exit after feedback

        else:
            print("Invalid choice! ❌ Try again.")

###############################################################################################################

main()