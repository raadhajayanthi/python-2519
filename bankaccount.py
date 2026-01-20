class Bankaccount():
    
   def __init__(self,balance,account_holder):
       self.__balance = balance
       self.__account_holder = account_holder
   
   def deposit(self,amount):
     if amount > 0:
      self.__balance += amount 
     else:
       print("no deposit amount")

   def withdraw(self,amount):
      if self.__balance >= amount:
        self.__balance = self.__balance - amount
      else:
       print("no sufficient amount")

   def get_balance(self):
     return self.__balance
   
   def get_account_holder(self):
     return self.__account_holder

banaccount_obj = Bankaccount(0,"raadha")
banaccount_obj.deposit(500)
banaccount_obj.withdraw(200)
print(banaccount_obj.get_balance())