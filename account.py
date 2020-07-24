from random import randint
from datetime import datetime


class Account:
    def __init__(self, account_first_name, account_last_name, account_email, account_phone_number, account_type):
        self.account_first_name = account_first_name.capitalize()
        self.account_last_name = account_last_name.capitalize()
        self.account_email = account_email
        self.account_phone_number = account_phone_number
        self.account_type = account_type

        self.account_pin = "0000"
        self.account_balance = 0
        self.account_number = self.generate_account_number()
        self.account_creation_timestamp = datetime.now()

    def __repr__(self):
        return f"{self.account_first_name} {self.account_last_name}\n{self.account_number}"

    def __str__(self):
        response = f"Account Info\n==============\n"
        response += f"Name: {self.account_first_name} {self.account_last_name}\n"
        response += f"Number: {self.account_number}\n"
        response += f"Email: {self.account_email}\n"
        response += f"Phone: {self.account_phone_number}\n"
        response += f"Type: {self.account_type}\n"
        response += f"Balance: {self.account_balance}\n"
        return response

    def changePin(self, pin):
        self.account_pin = pin

    def generate_account_number(self):
        account_number = ""
        for i in range(10):
            new_digit = str(randint(0, 9))
            account_number += new_digit

        return account_number

    def checkBalance(self):
        return self.account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

def run_test():
    act1 = Account("sam","dan", "samdan@gmail.com", "09034875548", "current")

    assert act1.account_first_name == "Sam", f"{act1.__repr__()}\nAccount first name don't match"
    assert act1.account_last_name == "Dan", f"{act1.__repr__()}\nAccount last name don't match"
    assert act1.account_email == "samdan@gmail.com", f"{act1.__repr__()}\nAccount email don't match"
    assert act1.account_type == "current", f"{act1.__repr__()}\nAccount type don't match"
    assert act1.account_pin == "0000", f"{act1.__repr__()}\nAccount pin don't match"
    assert act1.account_phone_number == "09034875548", f"{act1.__repr__()}\nAccount phone don't match"

    assert act1.checkBalance() == 0, f"{act1.__repr__()}\nbalance is not 0"
    assert act1.deposit(100) is None, f"{act1.__repr__()}\ndeposit failed"
    assert act1.checkBalance() == 100, f"{act1.__repr__()}\nbalance is not 100"
    assert act1.withdraw(50) is True, f"{act1.__repr__()}\nwithdrawal failed"
    assert act1.checkBalance() == 50, f"{act1.__repr__()}\nbalance is not 50"

    act2 = Account("Lola", "Ife", "lolaife@gmail.com", "09031755238", "savings")

    assert act2.account_first_name == "Lola", f"{act2.__repr__()}\nAccount first name don't match"
    assert act2.account_last_name == "Ife", f"{act2.__repr__()}\nAccount last name don't match"
    assert act2.account_email == "lolaife@gmail.com", f"{act2.__repr__()}\nAccount email don't match"
    assert act2.account_type == "savings", f"{act2.__repr__()}\nAccount type don't match"
    assert act2.account_pin == "0000", f"{act2.__repr__()}\nAccount pin don't match"
    assert act2.account_phone_number == "09031755238", f"{act2.__repr__()}\nAccount phone don't match"

    assert act2.checkBalance() == 0, f"{act2.__repr__()} balance is not 0"
    assert act2.deposit(500) is None, f"{act2.__repr__()} deposit Failed!"
    assert act2.checkBalance() == 500, f"{act2.__repr__()} balance is not 500"
    assert act2.transfer(act1, 250) is True, f"{act1.__repr__()} transfer Failed!"
    assert act2.checkBalance() == 250, f"{act2.__repr__()} balance is not 250"

    assert act1.checkBalance() == 300, f"{act1.__repr__()} balance is not 300"

    assert act2.changePin("1234") is None, f"{act2.__repr__()} change pin failed!"
    assert act2.account_pin == "1234", f"{act2.__repr__()} Pin is not 1234"

    print("\n===================All tests Passed!================================\n")

def main():
    sample_account = Account("iClass", "Chima", "iclasschima@gmail.com", "09031861100", "savings")
    print(sample_account)

    print(sample_account.__str__())

    print(sample_account.__repr__())

    run_test()

if __name__ == '__main__':
    main()