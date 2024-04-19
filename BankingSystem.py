from abc import ABC, abstractmethod

class BankingSystem(ABC):
    @abstractmethod
    def get_account_info(self):  #account operation
        pass

class Account(ABC):
    def __init__(self, account_type, balance, rate):
        self.account_type = account_type
        self.balance = balance
        self.rate = rate
    def get_account_type(self):
        pass
    
class SavingsAccount(Account, BankingSystem):
    def __init__(self, account_type, balance, rate):
        super().__init__(account_type, balance, rate)
        
    def get_account_type(self):
        return "Savings account"
    def get_account_info(self):
        print (f"Account type - {self.account_type}, Balance - {self.balance}")
        
class CheckingAccount(Account, BankingSystem):
    def __init__(self, account_type, balance, rate):
        super().__init__(account_type, balance, rate)
        
    def get_account_type(self):
        return "Checking account"
    def get_account_info(self):
        return f"Account type - {self.account_type}, Balance - {self.balance}"
    
class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        
    def customer_account(self, account):
        print(f"The customer {self.name} account is {account.get_account_type()}" )
    
class Transactions:
    def __init__(self, involved_acc, transaction_type, amount):
        self.involved_acc = involved_acc
        self.transaction_type = transaction_type
        self.amount = amount
    def get_customer(self, customer):
        print(f"{customer.name} starts a transaction")
    def get_account(self, account):
        print(f"Transaction was done by this account - {account.get_account_type()}")
        
customer1 = Customer("Ani", "Yerevan", 121314)
savings_account1 = SavingsAccount("Savings", 500, 30)
checking_account1 = CheckingAccount("Savings", 500, 30)
transactions1 = Transactions(savings_account1, "type", 1000)
customer1.customer_account(savings_account1)
print(checking_account1.get_account_info())



