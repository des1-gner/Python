# Stating our Savings Account Class
class SAccount:
    
    # Constructor / Initializer 
    def __init__(self, accNo, accNm, bal, maxAmt=500.00):
        self.__accNo = accNo
        self.__accNm = accNm
        self.__bal = bal
        self.__maxAmt = maxAmt
    
    def getaccNo(self):
        return self.__accNo
    
    def getaccNm(self):
        return self.__accNm
    
    def getbal(self):
        return self.__bal
    
    # success deposit
    def deposit(self, amount):
        self.__bal += float(amount)
        self.__bal = round(self.__bal, 2)
        print("Balance: $" + str(self.__bal))
        print("Deposit Successful!")
        print("---------------------------------")
        return True
    
    def withdraw(self, amount):
        # error         
        if float(amount) > self.__bal:
            print("Balance: $" + str(self.__bal))
            print("Withdrawal Amount is Greater than the Balance")
            print("Withdrawal Failed, Try Again.")
            print("---------------------------------")
            return False

        # error 2
        elif  float(amount) > self.__maxAmt:
            print("Maximum Amount: $" + str(self.__maxAmt))
            print("Withdraw Amount is Greater than the Maximum Amount")
            print("Withdraw Failed, Try Again.")
            print("---------------------------------")
            return False

        # success withdraw
        else:
            self.__bal -= float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: $" + str(self.__bal))
            print("Withdrawal Successful!")
            print("---------------------------------")
            return True

    # all necessary info for object account
    def __str__(self):
        return "Account Number: " + str(self.__accNo) + "\nAccount Name: " + self.__accNm + "\nBalance: $" + str(self.__bal) + "\nMinimum Amount: $" + str(self.__maxAmt)