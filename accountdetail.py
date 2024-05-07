
class Account:

    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    
    def debit_amount(self,amount):
        self.balance-=amount
        print("RS",amount,"is debited from your account")
        print("your totle balance is",self.check_balance())


    def credit_amount(self,amount):
        self.balance+=amount
        print("RS",amount,"is credited in your account")
        print("your totle balance is",self.check_balance())

    
    def check_balance(self):
        return self.balance



acc1 = Account(10000,23543553)

acc1.debit_amount(1000)
acc1.credit_amount(20000)