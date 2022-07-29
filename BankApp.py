from SAccountOOP import SAccount
from CAccountOOP import CAccount
import re

# Stating our Main Bank Class
class Bank:
    
    # Constructor / Initializer
    def __init__(self):
        self.__SAccount = []
        self.__CAccount = []
        self.__accIdx = -1
        self.__accObj = None
    # ^ as per the given Requirements
    
    def loadCAccount(self):
        #fr = load / opening of CAccounts.txt file
        # "r" = Open a file for reading. (default)
        fr = open("CAccounts.txt", "r")
        
        # for loop for repition
        for f in fr:
            #removes or truncates the given characters from the beginning and the end of the original string.
            f = f.rstrip("\n")
            # splits a string into a list
            temp = f.split(";")
            # returns the number of items in an object.
            if len(temp) == 3:
                p = CAccount(int(temp[0]), temp[1], float(temp[2]))
                self.__CAccount.append(p)
            else:
                p = CAccount(int(temp[0]), temp[1], float(temp[2]), float(temp[3]))
                self.__CAccount.append(p)

        fr.close()
    
    def loadSAccount(self):
        #fr = load / opening of SAccounts.txt file
        # "r" = Open a file for reading. (default)
        fr = open("SAccounts.txt", "r")
        
        # for loop for repition
        for f in fr:
            #removes or truncates the given characters from the beginning and the end of the original string.
            f = f.rstrip("\n")
            # splits a string into a list
            temp = f.split(";")
            # returns the number of items in an object.
            if len(temp) == 3:
                s = SAccount(int(temp[0]), temp[1], float(temp[2]))
                self.__SAccount.append(s)
            else:
                s = SAccount(int(temp[0]), temp[1], float(temp[2]), float(temp[3]))
                self.__SAccount.append(s)
            
        fr.close()
    # print watermark 
    print(f"---------Python Maxordia Financial----------")
    print(f"----Assessment Task 3: Python Project 2----")
    print(f"----Written by Oisin Aeonn S3952320 F2BE----")

    # Main Menu
    def menu(self):
        while True:
            print("------------------ Maxordia Financial: ------------------")
            print("1. Checking Account Options")
            print("2. Savings Account Options")
            print("3. View Checking Accounts")
            print("4. View Savings Accounts")
            print("5. Exit")
            print("---------------------------------------------------------")
            opt = input("Select Option: ")
            
            if opt == "1":
                accNo = input("Enter Checking Account Number: ")
                
                # error check
                if not accNo.isdigit():
                    print("Invalid input Entered for Account Number, Try again.")
                    self.menu()
                    
                self.__accIdx = self.getCAccount(accNo)
                
                # as per the requirements for success
                if self.__accIdx != -1:
                    # load checking menu
                    self.checkingMenu()
                    # another error
                else:
                    print("Checking Account does not Exist, Try again.")
            
            elif opt == "2":
                accNo = input("Enter Savings Account Number: ")

                # error    
                if not accNo.isdigit():
                    print("Invalid Input Entered for Savings Account Number, Try again.")
                    # go back to previous menu (again)
                    self.menu()
                
                self.__accIdx = self.getSAccount(accNo)
                
                # successful option selection
                if self.__accIdx != -1:
                    self.savingsMenu()
                # error 
                else:
                    print("Savings Account does not Exist, Try again.")
            
            # print checking account list
            elif opt == "3":
                print("------------------ Checking Accounts: ------------------")
                for s in self.__CAccount:
                    print(s)
                    print("************************")
                    print("---------------------------------------------------------")

            # print savings account list
            elif opt == "4":
                print("------------------ Savings Accounts: ------------------")
                for p in self.__SAccount:
                    print(p)
                    print("************************")

            # exit the application
            elif opt == "5":
                print("Thank You for Selecting Maxordia Financial, Have a Good Day!")
                exit()
                # error
            else:
                print("Invalid Option Selected, Try Again.")
    
    # Checking Account Menu
    def checkingMenu(self):
        self.__accObj = self.__CAccount[self.__accIdx]
                # while loop
        while True:            
            print("------------------ Checking Account: " + str(self.__accObj.getaccNo()) + " ------------------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Checking Account Details")
            print("5. Return to Main Menu")
            print("-----------------------------------------------------------------------------------------------")
            opt = input("Select Option: ")
            
            # deposit
            if opt == "1":
                amt = input("Enter Deposit Amount: $")
                
                # re.search module function import (regular expression) - searching for 2 digits that match, anchored and ending on line. 
                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    # calling our CAccountOOP.py functions within class for depositing 
                    self.__accObj.deposit(amt)
                    self.__CAccount[self.__accIdx] = self.__accObj
                    fw = open("BankingReceipt.txt", "w")
                    fw.write("----------------- Maxordia Financial -----------------")
                    fw.write("\nAccount Number: " + str(self.__accObj.getaccNo()))
                    fw.write("\nDeposit Amount: $" + amt)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                    fw.close()
                # error
                else:
                    print("Invalid Input Entered for Deposit Amount.")
                    print("Deposit Failed, Try Again.")
            # withdraw
            elif opt == "2":
                amt = input("Enter Withdrawal Amount: ")
                
                # re.search module function import (regular expression) - searching for 2 digits that match, anchored and ending on line. 
                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    # calling our CAccountOOP.py functions within class
                    status = self.__accObj.withdraw(amt) # for withdrawing
                    if status == True:
                        self.__CAccount[self.__accIdx] = self.__accObj
                        fw = open("BankingReceipt.txt", "w")
                        fw.write("----------------- Maxordia Financial -----------------")
                        fw.write("\nWithdrawal Amount: $" + amt)
                        fw.write("\nAccount Number: " + str(self.__accObj.getaccNo()))
                        fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                        fw.close()
                # error
                else:
                    print("Invalid Input Entered for Withdrawal Amount.")
                    print("Withdrawal Failed, Try Again.")
            
            # show current balance  
            elif opt == "3":
                print("Current Balance: $", self.__accObj.getbal())
                fw = open("BankingReceipt.txt", "w")
                fw.write("----------------- Maxordia Financial -----------------")
                fw.write("\nAccount Number: " + str(self.__accObj.getaccNo()))
                fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                fw.close()

            # print all necessary info for object account
            elif opt == "4":
                print("----------------- Checking Account Details: -----------------")
                print(self.__CAccount[self.__accIdx])
            
            # go back
            elif opt == "5":
                self.menu()
            # error
            else:
                print("Invalid Option Selected, Try again.")

    # Saving Account Menu
    def savingsMenu(self):
        self.__accObj = self.__SAccount[self.__accIdx]
        # while loop 
        while True:            
            print("------------------ Savings Account: " + str(self.__accObj.getaccNo()) + " ------------------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Savings Account Details")
            print("5. Return to Main Menu")
            print("-----------------------------------------------------------------------------------------------")
            opt = input("Select Option: ")
            
            # deposit
            if opt == "1":
                amt = input("Enter Deposit Amount: $")
                # re.search module function import (regular expression) - searching for 2 digits that match, anchored and ending on line. 
                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    # calling our SAccountOOP.py functions within class
                    self.__accObj.deposit(amt) # for depositing 
                    self.__SAccount[self.__accIdx] = self.__accObj
                    fw = open("BankingReceipt.txt", "w")
                    fw.write("----------------- Maxordia Financial -----------------")
                    fw.write("\nAccount Number: " + str(self.__accObj.getaccNo()))
                    fw.write("\nDeposit Amount: $" + amt)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                    fw.close()
                else:
                    print("Invalid Input Entered for Deposit Amount.")
                    print("Deposit Failed, Try Again.")
            
            elif opt == "2":
                amt = input("Enter Withdrawal Amount: ")
                # re.search module function import (regular expression) - searching for 2 digits that match, anchored and ending on line. 
                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    # calling our SAccountOOP.py functions within class
                    status = self.__accObj.withdraw(amt) # for withdrawing
                    self.__SAccount[self.__accIdx] = self.__accObj
                    if status == True:
                        self.__SAccount[self.__accIdx] = self.__accObj
                        fw = open("BankingReceipt.txt", "w")
                        fw.write("----------------- Maxordia Financial -----------------")
                        fw.write("\nWithdrawal Amount: $" + amt)
                        fw.write("\nAccount Number: " + str(self.__accObj.getaccNo()))
                        fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                        fw.close()
                # error 
                else:
                    print("Invalid Input Entered for Withdrawal Amount.")
                    print("Withdrawal Failed, Try Again.")
            
            # check balance
            elif opt == "3":
                print("Current Balance: $", self.__accObj.getbal())
                fw = open("BankingReceipt.txt", "w")
                fw.write("----------------- Maxordia Financial -----------------")
                fw.write("\nCard Number: " + str(self.__accObj.getaccNo()))
                fw.write("\nCurrent Balance: $" + str(self.__accObj.getbal()))
                fw.close()
            
            # print all necessary info for object account
            elif opt == "4":
                print("----------------- Savings Account: -----------------")
                print(self.__SAccount[self.__accIdx])
            
            # go back
            elif opt == "5":
                self.menu()
            # error
            else:
                print("Invalid Option Selected, Try again.")
    # function for getting account per the UML Diagram
    def getCAccount(self, accNo):
        for p in self.__CAccount:
            if int(accNo) == p.getaccNo():
                return self.__CAccount.index(p)
        
        return -1

    # function for getting account per the UML Diagram
    def getSAccount(self, accNo):
        for s in self.__SAccount:
            if int(accNo) == s.getaccNo():
                return self.__SAccount.index(s)

        return -1
    # run time
    def main(self):
        self.loadSAccount()
        self.loadCAccount()
        self.menu()

run = Bank()
run.main()