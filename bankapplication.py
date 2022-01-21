class Bank:

    def __init__(self):
        self.closingBal = 0


    def display(self):
        print("Enter your options:")
        print("1 for deposit :\n2 for withdraw:")
        getoption = input()

        if getoption == "1":
            self.deposit()
        elif getoption == "2":
            self.withdraw()
        elif getoption !=1 or getoption !=2:
            print("thanks")
            return
        print("your closing balance is :",self.closingBal)
        print("do you want to continue Y for Yes for exit press any key:")
        a = input()
        if a == "Y" or a == "y":
            self.display()
        else:
            print("thanks for visiting our bank")


    def deposit(self):
        depositamount = int(input("enter your deposit amount:"))
        self.closingBal = self.closingBal + depositamount
        return self.closingBal
    def withdraw(self):
        withdramount = int(input("Enter your withdraw amount:"))
        if self.closingBal >= withdramount:
            self.closingBal = self.closingBal - withdramount
            print("after withdraw your balance amount is :",self.closingBal)
        else:
            print("no suffient balance")
        return self.closingBal
bank = Bank()
bank.display()

