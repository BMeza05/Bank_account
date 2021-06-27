
class User:
    def __init__(self, name, email, bank_name):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.bank_name = bank_name

class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        balance == 0
        int_rate = .03
    
    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def display_account_info(self):
        self.balance
        print(self.balance)

    def yield_interest(self, int_rate):
        self.balance // int_rate

gordon = User("Gordon Ramsay", "gr@gmail.com", "Bank of angry chefs" )
bruce = User("bruce Wayne", "notbatman@outlook.com", "Bank of men dressed in bat suits")

print (gordon.name)
print(bruce.name)

gordon = BankAccount("Gordon Ramsay", 0)
bruce = BankAccount("Bruce Wayne", 0 )
print(gordon.balance)

gordon.make_deposit(10)
gordon.make_deposit(15)
gordon.make_deposit(10)
gordon.display_account_info
print(gordon.balance)

gordon.yield_interest
print(gordon.balance)

bruce.make_deposit(20)
bruce.make_deposit(20)
bruce.make_withdrawl(1)
bruce.make_withdrawl(1)
bruce.make_withdrawl(1)
bruce.make_withdrawl(1)
bruce.display_account_info
print(bruce.balance)