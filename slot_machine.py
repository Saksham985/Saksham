# SLOT MACHINE GAME

def display():

    print('****************************************************')
    print('**                                                **')
    print('**       WELCOME TO THE SLOT MACHINE GAME         **')
    print('**                                                **')
    print('**     Try your luck and win big prizes!          **')
    print('**                                                **')
    print('**    1. Start the Game (press "s)                **')
    print('**    2. Exit (press "e")                         **')
    print('**    3. Feedback & review (press "f")            **')
    print('**                                                **')
    print('****************************************************')

import random
import time 


#################################################################################################################


def spin_row():

    symbols = ['💎', '👑', '💰']
    return [random.choice(symbols) for _ in range(3)]

#################################################################################################################


def print_row(row):

    print('*************')
    print(' | '.join(row))
    print('*************')

#################################################################################################################


def get_payout(row,bet):

    if row[0] == row[1] == row[2]:
        if row[0] == '💎':
            return bet * 5
        elif row[0] == '👑':
            return bet * 4
        elif row[0] == '💰':
            return bet * 3
    return 0

#################################################################################################################


def main():

    while True:
        display()
        choice = input("\nEnter your choice: ").lower()

        if choice == 's':
            balance = 100
            print("\n+---------------- Python Slot Machine --------------------+")
            print('+                                                         +')
            print('+        Symbols : 💎 👑 💰                               +')
            print('+                                                         +')
            print('+---------------------------------------------------------+')

            while balance > 0:
                print(f'Your Current balance ₹{balance}')

                bet  = input("\nPlace your bet amount : ₹ ")

                if not bet.isdigit():
                    print("Please enter a valid bet amount 😑")
                    continue

                bet = int(bet)

                if bet > balance:
                    print('Insufficient Funds 💸')
                    continue

                if bet <= 0:
                    print("Bet amount must be greater than zero")
                    continue

                balance -= bet

                row = spin_row()

                print("\nSpinning in ...⌛")
                for x in range(3,0,-1):
                    seconds = x % 60
                    print(f'{seconds:02}')
                    time.sleep(1)
                print()
                print_row(row)


                payout = get_payout(row,bet)

                if payout > 0:
                    print(f'You win the round 🎉 REWARD :  ₹ {payout}')
                else:
                    print('You lost 😭. Better Luck Next Time 👍')

                balance += payout

                play_again = input("\nDo you want to play again (y/n) ☺️ : ").lower()
                if play_again != 'y':
                    print(f'\nThanks for playing 👋. Your balance ₹ {balance}\n')
                    break

                    
        elif choice == 'e':
            print("Exiting the game. Goodbye! 👋")
            break

        elif choice == 'f':
            print("\nRedirecting to feedback and review section")
            
            for i in range(3):
                print("Loading" + "." * (i+1))
                time.sleep(0.5)
            print()
            rating = float(input("How much do you rate us out of 5 ? : "))
            provide = input("Please provide feedback for improvements : \n")
            print()
            print(f'''We appriciate your ratings 👍 {rating}/5 
    Thanks for the feed back we will work on it ✅''')
                
        else:
            print("\nInvalid choice 🤔. Please Try Again --> \n")
        
#################################################################################################################
  
main()






    
    
