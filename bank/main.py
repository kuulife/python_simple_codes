class Bank():
	def __init__(self,owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self,dep_amount):
		self.balance += dep_amount
		print(f'deposit accepted added {dep_amount}$ to the balance\n')

	def withdraw(self,w_balance):
		if w_balance <= self.balance:
			self.balance -= w_balance
			print('withdraw accepted\n')
		else:
			print('balance is not available')
	
	def __str__(self):
		return f'Owner: {self.owner} \nBalance : {self.balance}$\n'

account = Bank('kutman',70000)
print(account)
account.deposit(1)
print(account)
account.withdraw(70000)
print(account)
