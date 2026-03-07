from abc import ABC, abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("You can check Your bank Balanace")
    @abstractmethod
    def deposite(self):
        pass 
    @abstractmethod
    def withdraw(self):
        pass 
class SavingAccount(BankAccount):
    def deposite(self):
        print('2 Laakh per day')
    def withdraw(self):
        print('You can withdraw 1 lakh')
class CurrentAccount(BankAccount):
    def deposite(self):
        print('No Limit ')
    def withdraw(self):
        print('No Limit ')
class jointAccount(BankAccount):
    def deposite(self):
        print('You can deposite 5 Lakh')
    def withdraw(self):
        print('You can Withdrew 2 lakh')
class SalaryAccount(BankAccount):
    def deposite(self):
        print('10 Laakh per day')
    def withdraw(self):
        print('You can withdraw 3 lakh')
class PensionAccount(BankAccount):
    def deposite(self):
        print('1 Laakh per day')
    def withdraw(self):
        print('You can withdraw 50k')
print("------------------Abhi---------------")
abhi = SavingAccount()
abhi.checkbalance()
abhi.deposite()
abhi.withdraw()
print("------------------swapnil---------------")
swapnil = CurrentAccount()
abhi.checkbalance()
abhi.deposite()
abhi.withdraw()
print("------------------s_n---------------")
s_n = jointAccount()
s_n.checkbalance()
s_n.deposite()
s_n.withdraw()
print("------------------praveen---------------")
praveen = PensionAccount()
praveen.checkbalance()
praveen.deposite()
praveen.withdraw()