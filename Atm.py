class ATM(object):
    # Making Constructor
    def __inti__(self, balance, atmNumber, pin, amount, amountLeft):
        self.balance = balance
        self.atmNumber = atmNumber
        self.pin = pin
        self.amount = amount
        self.amountLeft = amountLeft

    # Writing Some Text
    print("---------------------------------------------------BANK ATM---------------------------------------------------")
    print("Don't Worry, It is very very safe")
    print()

    # Asking Your Name
    name = input("Enter Your Name: ")

    # Creating The Main Function
    def main(self):
        # Greeting The User
        print("Hello " + self.name + ",")
        print("Just Enter The Following Details")
        print()

        # Calling The Function UpdatingValues()
        self.updatingValues()
        
        # Shortening The Parameters That Are There In The Constructor
        parameter1 = self.balance
        parameter4 = self.amount

        if parameter1 >= parameter4:
            self.CashWithdrawn()
        else:
            self.CashNotWithdrawn()

    def updatingValues(self):
        # Taking All The Inputs From The User
        bankBalance = int(input("Enter Your Bank Balance: Rs. "))
        atmNum = input("Enter Your ATM Card Number: ")
        atmPin = int(input("Enter Your ATM Pin: "))
        withdrawCash = int(input("Enter Amount To Be Withdrawn: Rs. "))

        # Updating The Bank Balance
        newBankBalance = bankBalance - withdrawCash

        # Updating Values In Constructor
        self.balance = bankBalance
        self.atmNumber = atmNum
        self.pin = atmPin
        self.amount = withdrawCash
        self.amountLeft = newBankBalance

    def CashWithdrawn(self):
        parameter1 = self.balance
        parameter2 = self.atmNumber
        parameter3 = self.pin
        parameter4 = self.amount
        parameter5 = self.amountLeft

        print()
        print("--------------------------------------------------------------------------")
        print("Cash Withdrawn!!")
        print()
        print("So These Are Your Entered Details:-")
        print("Your ATM Card No.: " + parameter2)
        print("Your ATM Pin: " + str(parameter3))
        print("Your Previous Bank Balance: " + str(parameter1))
        print("Your Withdrawn Amount: " + str(parameter4))
        print("Your Left Amount In The Bank: " + str(parameter5))

    def CashNotWithdrawn(self):
        parameter1 = self.balance
        parameter4 = self.amount
        parameter5 = self.amountLeft
        
        print()
        print("--------------------------------------------------------------------------")
        print("Your Bank Balance Is: " + str(parameter1))
        print("Your Withdrawn Amount: " + str(parameter4))
        print("Your Amount That Would Be Left In The Bank: " + str(parameter5) + ". YOU WOULD BE IN DEBT")
        print("Can't Proceed!")
        print("Please Enter Again!")
        print()

        # Calling The Function Taking Input Again
        self.EnterCredentialsAgain()

    def EnterCredentialsAgain(self):
        # Taking All The Inputs From The User
        bankBalance = int(input("Enter Your Bank Balance: Rs. "))
        withdrawCash = int(input("Enter Amount To Be Withdrawn: Rs. "))

        # Updating The Bank Balance
        newBankBalance = bankBalance - withdrawCash

        # Updating Values In Constructor
        self.balance = bankBalance
        self.amount = withdrawCash
        self.amountLeft = newBankBalance

        # Shortening The Parameters That Are There In The Constructor
        parameter1 = self.balance
        parameter4 = self.amount

        if parameter1 >= parameter4:
            self.CashWithdrawn()
        else:
            self.CashNotWithdrawn()

defineClass = ATM()
defineClass.main()