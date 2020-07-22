class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount)< 0:
            print("Insufficient funds: Charging a $5")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: $"+str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.int_rate)
        return self

Account1 = BankAccount(.01,100)
Account2 = BankAccount(.04,100)

Account1.deposit(100).deposit(100).deposit(300).withdraw(50).yield_interest().display_account_info()
Account2.deposit(10000000).deposit(1500000).withdraw(4500).withdraw(70000).withdraw(95000).withdraw(84000).yield_interest().display_account_info()
