# ROCK,PAPER,SCISSOR GAME

import random

print("Welcome to Rock, Paper, Scissor Game!")

emojis = {
    'r': '✊',  # Rock
    'p': '✋',  # Paper
    's': '✌️'   # Scissor
}

while True:
    user_choice = input("ROCK,PAPER,SCISSOR (r/p/s): ").lower()
    if user_choice not in ['r','p','s']:
        print("Invalid input! Please choose 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(['r','p','s'])

    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")   

    elif ((user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Starting a new game...")
