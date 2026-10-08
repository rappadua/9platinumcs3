class BankAccount:
def __init__(self, account_number: int, balance: float):
#Private attributes
self.__account_number = account_number
self.__balance =0.0

#Use setters to initialize value safely
self.set_account_number(account_number)
self.set_balance(balance)

#Setter methods
def set_account_number(self, account_number: int):
self,__accounnt_number = account_number

def set_balance(self, balance: float):
if balance < 0:
print("The balance must not be a negative number.")
else:
self.__balance = float(balance)

#Getter methods using @property decorator
@property
def account_number(self) -> int:
return self.__account_number

@property
def balance(self) -> float:
return self.__balance

#Additional standard getters matching UML diagram requirements
def get_account_number(self) -> int:
return self.__account_number

def get_balance(self) -> float:
return self.__balance

#Demonstration matching the sample output
if __name__ == "__main__":
#Create a BankAccount object
a1 = BankAccount(12345, 1000)

print("Account 1")
print(f"Account Number: {a1.account_number}")
print((f"Balance: {a1.balance:.2f}\n"))

print("Update balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}\n")
