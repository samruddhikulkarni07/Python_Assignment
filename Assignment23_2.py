class BankAccount:

    ROI = 10.5

    def __init__(self,N,B):
        self.Name = N
        self.Amount = B

    def Display(self): 
        print("Account holder name :",self.Name)
        print("Current Balance is :",self.Amount)

    def Deposit(self):
        deposit = int(input("How many amount you want to deposite:"))

        self.Amount = self.Amount + deposit
        print("Your total bank balance is:",self.Amount)

    def Withdraw(self):
        withdraw = int(input("How many amount you want to withdraw:"))

        if(self.Amount>withdraw):
            self.Amount = self.Amount - withdraw
            print("Your total bank balance is:",self.Amount)

        else:
            print("You have insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Your interest is:",Interest)


obj1 = BankAccount("Soham",1000)
obj2 = BankAccount("Radha",2000)
obj3 = BankAccount("Priya",3000)
obj4 = BankAccount("Gatha",5000)

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
print("\n")

obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
print("\n")

obj3.Display()
obj3.Deposit()
obj3.Withdraw()
obj3.CalculateInterest()
print("\n")

obj4.Display()
obj4.Deposit()
obj4.Withdraw()
obj4.CalculateInterest()
print("\n")