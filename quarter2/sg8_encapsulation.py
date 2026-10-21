#create the class named "BankAccount"
class BankAccount:
  #intialize the private attributes by using double underscores
  def __init__(self, account_number: int, balance: float):
    #Private attributes
    self.__account_number = account_number
    self.__balance =0.0
    #it passes initial values through setter methods to make sure validation rules apply
    self.set_account_number(account_number)
    self.set_balance(balance)
    
#Setter methods
#this is the Public Setter method for account_number
def set_account_number(self, account_number: int):
  #directly update the private attribute __account_number
  self,__accounnt_number = account_number
#the Public Setter method for balance with validation logic
def set_balance(self, balance: float):
  #check if the balance is negative
  if balance < 0:
    #give out a warning message and then ignore the invalid update
    print("The balance must not be a negative number.")
  else:
    #if it is valid (can be 0 or positive), convert to float and store in private attribute
    self.__balance = float(balance)

#Getter methods using @property decorator
#@property decorator allows reading private attributes by using dot notation 
@property
def account_number(self) -> int:
  #return the private account number
  return self.__account_number

@property
def balance(self) -> float:
#Print initial details matching the requested sample output format  #return the private balance
  return self.__balance

#Additional standard getters matching UML diagram requirements
def get_account_number(self) -> int:
  return self.__account_number

def get_balance(self) -> float:
  return self.__balance

#Demonstration matching the sample output
if __name__ == "__main__":
#make a BankAccount object with the examples "account_number=12345 and balance=1000"
  a1 = BankAccount(12345, 1000)
#print the initial details matching the requested sample output format
print("Account 1")
#acces the private attributes securley using property getters
print(f"Account Number: {a1.account_number}")
#format the balance as a float with 2 decimal places
print((f"Balance: {a1.balance:.2f}\n"))

#it's going to attempt to update balance with a negative value to test validation
print("Update balance to -100")
a1.set_balance(-100)
#lastly, print the details again to show balance remained unchanged at 1000.00
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}\n")
