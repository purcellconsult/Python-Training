# OOP in python
# --------------
# oop is a style of programming
# encourages coding using classes and objects
# great for code reuse
# python allows oop programming in addition to procedural
# lots of new terms!
# method looks like a function, except it's binded to a class
# self is not a keyword, it's a convention. Denotes instance variable
# to define a class in python use the 'class' keyword
# an instance of a class is when you create a copy of it


class BankAccount:
    """
    This is an example of oop programming using a
    bank account.
    """
    def __init__(self, deposit, bankaccount_number):
        self.balance = 0
        if deposit > 0 and deposit <= 5000:
            self.balance = deposit
        else:
            print('Invalid input')
            exit(0)

    def make_deposit(self, amount):
        if amount > 0 and amount <= 5000:
                self.balance += amount
        else:
            print('Invalid input')
            exit(0)

    def withdraw(self, amount):
        if self.balance < 0 or self.balance == 0:
            print('You have $0, time to close account!')
            return
        elif self.balance - amount > 0:
            self.balance -= amount
            return self.balance
        else:
            print('Only have $ {}'.format(self.balance))


    def get_balance(self):
        return self.balance

    def print_balance(self):
        print(self.balance)


if __name__ == '__main__':
    account_one = BankAccount(5000, '123-3773-282')
    account_one.make_deposit(1000)
    account_one.withdraw(500)
