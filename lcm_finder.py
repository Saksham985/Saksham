# FINDING LCM OF N NUMBERS (INPUT BY USER) , USING ABS AND GCD MODULE OF MATH

def lcm():

    import math

    while True:
        num = int(input("LCM of how many numbers you want to find: "))
        print()
        lst = []
        for i in range(num):
            x = int(input(f"Enter number {i+1}: "))
            lst.append(x)
        
        # start with first number
        lcm = lst[0]
        
        # loop to find LCM of all numbers
        for i in lst[1:]:
            lcm = lcm * i // math.gcd(lcm, i)
        print()
        print("The LCM of the given numbers is:", lcm)

        choice = input("\nDo you want to find LCM of more numbers? (y/n): ").lower()
        if choice != 'y':
            print("\nThank you for using the LCM finder!")
            break

lcm()