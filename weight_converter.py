# WEIGHT CONVERTER 

def instructions():
    print('***************** Mandatory Instructions *******************')
    print('*                                                          *')
    print("*          Welcome to the Weight Converter!                *")
    print("*          You can convert weights between these units.    *")
    print("*          kilogram (kg) , Pound (lb)  , Tonne (ton)       *")
    print("*          For kg <--> lb press 1                          *")
    print("*          For kg <--> ton press 2                         *")
    print("*          For lb <--> ton press 3                         *")
    print("*          Type 'exit' to quit the program.                *")
    print('*                                                          *')
    print('************************************************************') 

instructions()

while True:
    choice = input("\nEnter your choice (1/2/3) or exit : ")

    if choice == 'exit':
        print('Exited successfully ...')
        break

    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please try again.\n")
        continue

    if choice == '1':
        print('\n----------------------------------------------')
        weight = float(input("\nEnter the weight : "))
        unit = input("Given weight is in kg OR lb : ").lower()
        print(f'\nEntered weight is {weight} {unit}')

        if unit == 'kg':
            converted_weight = weight * 2.20462 
            converted_weight = round(converted_weight,3)
            print(f'Weight into pounds = {converted_weight} lbs')
            print('\n----------------------------------------------')

        else:
            converted_weight = weight/2.20462
            converted_weight = round(converted_weight,3)
            print(f'Weight into kg = {converted_weight} kg')
            print('\n----------------------------------------------')
            
        truncate = input('\nWant to exit ? (y/n) :').lower()
        if truncate == 'y':
            print('Exited successfully ...')
            break
        
    elif choice == '2':
        print('\n----------------------------------------------')
        weight = float(input("\nEnter the wieght : "))
        unit = input("Given weight is in kg OR ton : ").lower()
        print(f'\nEntered weight is {weight} {unit}')

        if unit == 'kg':
            converted_weight = weight/1000
            print(f'Weight into tonnes = {converted_weight} ton')
            print('\n----------------------------------------------')
        else:
            converted_weight = weight*1000
            converted_weight = round(converted_weight,5)
            print(f'Weight into kilograms = {converted_weight} kg')
            print('\n----------------------------------------------')

        truncate = input('\nWant to exit ? (y/n) :').lower()
        if truncate == 'y':
            print('Exited successfully ...')
            break

    else:
        print('\n----------------------------------------------')
        weight = float(input("\nEnter the weight :"))
        unit = input("Given weight is in lb OR ton ? : ").lower()
        print(f'\nEntered weight is {weight} {unit}')

        if unit == 'lb':
            converted_weight = weight/2000
            print(f'weight into tons = {converted_weight} tons')
            print('\n----------------------------------------------')
        else:
            converted_weight = weight*2000
            converted_weight = round(converted_weight,4)
            print(f'approx weight into pounds = {converted_weight} lbs')
            print('\n----------------------------------------------')
        
        truncate = input('Want to exit ? (y/n) :').lower()
        if truncate == 'y':
            print('Exited successfully ...')
            break