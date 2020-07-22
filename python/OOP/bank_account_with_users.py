class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount)< 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.int_rate)
        return self

class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.05, balance=0)
        #adding the deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        #adding withdrawl method
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
        #display balance me
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
        #transfer money bonus
    def transfer_money(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

# Account1 = BankAccount(.01,100)
# Account2 = BankAccount(.04,100)

# Account1.deposit(100).deposit(100).deposit(300).withdraw(50).yield_interest().display_account_info()
# Account2.deposit(10000000).deposit(1500000).withdraw(4500).withdraw(70000).withdraw(95000).withdraw(84000).yield_interest().display_account_info()

garrett = User("Garrett Bass","gbass1912@gmail.com")
nick = User("Nick McMayon", "nick.mcmayon@something.com")

garrett.make_deposit(100000).transfer_money(nick, 12354).account.yield_interest().display_account_info()

nick.display_user_balance()

