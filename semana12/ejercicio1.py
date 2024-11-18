class BankAccount: 
  def __init__(self, balance):
    self.balance = balance

  def withdraw_money(self, withdraw_ammount):
    if self.balance >= withdraw_ammount:  
      self.balance -= withdraw_ammount  
      return self.balance
    else:
      return "Insufficient money"
  
  def enter_money(self, enter_ammount):
    self.balance += enter_ammount  
    return self.balance

class SavingsAccount(BankAccount): 
  def __init__(self, balance, min_balance):
    super().__init__(balance)
    self.min_balance = min_balance  

  def withdraw_money(self, withdraw_ammount):
    if self.balance - withdraw_ammount < self.min_balance:  
      return "Not enough money to maintain the minimum balance"
    else:
      return super().withdraw_money(withdraw_ammount)
    
account = SavingsAccount(1000, 200)
print(account.withdraw_money(900)) 
print(account.withdraw_money(300))  
account.enter_money(500)
print(account.balance)  