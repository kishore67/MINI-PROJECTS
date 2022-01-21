class Bank:

    def __init__(self):
        self.closingBal = 0 # coustomer closing blance is 0


    def display(self):
        print("Enter your options:")
        print("1 for deposit :\n2 for withdraw:") # enter the option what you want to do(withdraw or deposit)
        getoption = input()

        if getoption == "1": # if you enter 1 then deposit function will call
            self.deposit()    
        elif getoption == "2": # if you enter 2 then withdraw function will call
            self.withdraw()
        elif getoption !=1 or getoption !=2: # if the input is nor 1 or neither 2 then it will print thanks
            print("thanks")
            return
        print("your closing balance is :",self.closingBal)
        print("do you want to continue Y for Yes for exit press any key:")
        a = input()
        if a == "Y" or a == "y":
            self.display()
        else:
            print("thanks for visiting our bank")


    def deposit(self): # this method is used to deposit our money in bank
        depositamount = int(input("enter your deposit amount:")) 
        self.closingBal = self.closingBal + depositamount
        return self.closingBal
    def withdraw(self): #this  is for withdraw 
        withdramount = int(input("Enter your withdraw amount:"))
        if self.closingBal >= withdramount:
            self.closingBal = self.closingBal - withdramount
            print("after withdraw your balance amount is :",self.closingBal)
        else:
            print("no suffient balance")
        return self.closingBal
bank = Bank()
bank.display()

