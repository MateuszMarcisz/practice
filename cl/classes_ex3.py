class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount >= 0.0:
            self.cash += amount
            print(f"You deposited {amount} cash. Your balance is {self.cash}")
        else:
            print("HUH? You ok, mate?")

    def withdraw_cash(self, amount):
        if amount > 0.0:
            if amount <= self.cash:
                self.cash -= amount
                print(f"{amount} cash withdrawn, {self.cash} left in the bank.")
            else:
                print(f"You didn't have enough money in the bank. {self.cash} cash withdrawn, nothing left in the bank.")
                self.cash = 0.0
        else:
            print("What do you think you're doin mate?")

    def print_info(self):
        print(f"Bank Account: {self.number}, Balance: {self.cash}")


acc1 = BankAccount(1)
acc1.deposit_cash(100)
acc1.print_info()
acc1.deposit_cash(-100)
acc1.withdraw_cash(200)
acc1.print_info()
acc1.deposit_cash(200)
acc1.print_info()
acc1.withdraw_cash(-200)
acc1.deposit_cash(100)


