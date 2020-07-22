class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        #adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        #adding withdrawl method
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
        #display balance me
    def display_user_balance(self):
        print("User: "+ self.name +", Balance: $"+str(self.account_balance))
        return self
        #transfer money bonus
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
garrett = User("Garrett Bass", "gbass1912@something.com")

guido.make_deposit(100).make_deposit(75).make_deposit(100).make_withdrawl(75).display_user_balance()

garrett.make_deposit(15000000).make_withdrawl(10000).make_withdrawl(25000).make_withdrawl(1000).transfer_money(monty, 3000).display_user_balance()

monty.make_deposit(1000).make_deposit(2000).make_withdrawl(1500).display_user_balance()



