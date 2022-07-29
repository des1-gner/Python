
# REQUIRES NUMPY ADDITIONAL LIBRARY.
# py -m pip install numpy
# generate random integer values
from tkinter import Pack
from numpy.random import seed
from numpy.random import randint
def Fruit_Market():
    def Cost():
        print("Welcome to the Fruit Market!")
        
        #Fruit Prices
        Strawberry_Price = 0.0156
        Banana_Price = 0.0049
        
        #User Inputed Quantities
        Strawberry_Quantity = input("How many grams of Strawberries would you like?: ")
        Banana_Quantity = input("How many grams of Bananas would you like?: ")

        #
        Banana_Total = int(Banana_Quantity) * Banana_Price
        Strawberry_Total = int(Strawberry_Quantity) * Strawberry_Price

        Total = Strawberry_Total + Banana_Total

    def Payment():
        Payment_Type = input(f"Your total comes to ${Cost().Total}, would you like to pay cash or credit card? ")
        Payment_Type.lower

        if Payment_Type == "cash":
            print(f"*You give the cashier ${Cost().Total}*")
            Payment_Success = True

        elif Payment_Type == "credit" or "credit card" or "card":
            print(f"*You tap your credit card for a total of ${Cost().Total}*")
            Payment_Success = True

        else:
            print("""ERRORCODE 01
            Payment Type invalid. 
            Please try again.
            """)
            Payment_Success = False

        if Payment_Success == True:
            # seed random number generator
            seed(1)
            # generate some integers
            Receipt_Number = randint(0, 10, 13)
            print(f"Your reciept number is {Receipt_Number}")
            print("Thank you for shopping with us!")
            Restart = input("Come again?:" )
                
            if Restart.lower == "yes":
                Fruit_Market()

            elif Restart.lower == "no":
                exit
        else:
            Payment()  


Fruit_Market()
Fruit_Market().Payment()



    

 
