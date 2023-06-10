class Bank:
    def __init__(self)-> None:
        self.users = {}
        self.accounts = []
        self.is_loan_enabled = True
        self.total_loan_amount = 0              
        self.total_balance = 0

    def create_account(self, name, initial_balance):
        account = Account(name, initial_balance)
        self.accounts.append(account)
        return account

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return total_balance

    def get_total_loan_amount(self):        
        return self.total_loan_amount

    def loan_feature(self, enabled):
        self.is_loan_enabled = enabled

    def perform_loan(self, account):
        loan_amount = account.balance * 2
        self.total_loan_amount += loan_amount
        account.deposit(loan_amount)
        return loan_amount


class Account:
    def __init__(self, name, initial_balance)-> None:
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            return True
        return False

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            return True
        return False

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):             
        return self.transaction_history



bank = Bank()


bank.create_account("admin", 500)  
print(bank.get_total_balance())


Abdul = bank.create_account("Abdul", 5000)
Abdul2 = bank.create_account("Abdul2", 500)
Abdul3 = bank.create_account("Abdul3", 50000)


Abdul.deposit(500)
Abdul.withdraw(200)
Abdul2.deposit(100)
Abdul2.withdraw(150)
Abdul3.deposit(200)
Abdul3.withdraw(50)


Abdul.transfer(Abdul2, 300)
Abdul2.transfer(Abdul3,50)


print(Abdul.check_balance())  
print(Abdul2.check_balance())
print(Abdul3.check_balance())


print(Abdul.get_transaction_history()) 
print(Abdul2.get_transaction_history())
print(Abdul3.get_transaction_history()) 


print(bank.get_total_balance()) 
print(bank.get_total_loan_amount()) 


bank.loan_feature(True)


loan_amount = bank.perform_loan(Abdul)
print(loan_amount)


print(bank.get_total_loan_amount())
