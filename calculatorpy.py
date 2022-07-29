# Watermark / Menu 

print("""
Python Calculator
Assessment Task 2: Python Project 1
Written by Oisin Aeonn F2BE
""")

def Menu():
    print("""
    Menu: 
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Exit
    """)

def Math():
    Menu_Selection = input("Input Operation Type: ")
    Allowed_Choices = ("1", "2", "3", "4")
    
    if Menu_Selection in Allowed_Choices:
        Number_1 = int(input("Input First Value: "))
        Number_2 = int(input("Input Second Value: "))

        # Addition
    if Menu_Selection == "1":
            Total = Number_1 + Number_2
            print(f"{Number_1} + {Number_2} = {Total}")
            Restart()

        # Subtraction
    elif Menu_Selection == "2":
            Total = Number_1 - Number_2
            print(f"{Number_1} - {Number_2} = {Total}")
            Restart()

        # Multiplication
    elif Menu_Selection == "3":
            Total = Number_1 * Number_2
            print(f"{Number_1} * {Number_2} = {Total}")
            Restart()

    # Division
    elif Menu_Selection == "4":
        if Number_2 == 0:
            print("Cannot divide by zero")
            Math()
            Menu()

        else: 
            Total = Number_1 / Number_2
            print(f"{Number_1} / {Number_2} = {Total}")
            Restart() 

    # Exit
    elif Menu_Selection == "5":
        print("Thank You For Using This Program!")
        quit()

    # Error
    else:
        print("""
        Invalid Selection Input
        Please Try Again
        """)
        Menu()
        Math()

# Ask User If They Need To Calculate More
def Restart():
    Calculate_Again = input("Calculate Again? (yes/no): ")
    Calculate_Again.lower
    
    if Calculate_Again == "yes":
        Menu()
        Math()

    elif Calculate_Again == "no":
        print("Thank You For Using This Program!")
        quit()

    # Error
    else: 
        print("""
        Invalid Selection Input
        Please Try Again
        """)
        Restart()

# Runtime Sequence
Menu()
Math()
