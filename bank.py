from datetime import datetime

class Account:
    
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transactionfee= 30
        self.loanlimit=1000
        self.loan=0
    
        self.transactions=[]#create a  dictionary to store transactions

        
        
    def deposit(self,amount):
        try:
            amount+10
        except TypeError:
            return f"please enter amount in digits"    
        if amount <=0:
            print ("Enter a valid amount")
        else:
            self.balance=self.balance+amount
            transaction1={'amount':amount,'balance':self.balance,'narration':"You deposited",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"{self.name} you have deposited {amount} your new balance is {self.balance}"

   
   
    def widthdraw(self , amount)  :
        try:
            amount+10
        except TypeError:
            return f"please enter amount in digits" 

        
        total=amount+self.transactionfee
        if  self.balance== 0:
          
            return f"{self.name} you have insufficient balance in your accout to make this transaction " 
            
        elif total>self.balance:
            return f"{self.name} your account balance {self.balance} is not enough to support transaction fee"

        elif total<self.balance:
            self.balance=self.balance-total
            
            transaction1={'amount':amount,'balance':self.balance,'narration':"You Withdrew",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"{self.name} you have sucessfully withdrawn  {amount} from your account with a fee of {self.transactionfee}.Your new balance is {self.balance}"
    
    
    def borrow(self,amount) :

        try:
            amount+10
        except TypeError:
            return f"please enter amount in digits" 
           
            
        if amount<=0:
             return f"unsucessful!Amount requested {amount} is below 0 your current loan limit is {self.loanlimit}"

        elif self.loan>0:
            return f"Failed you have an existing loan of {self.loan}"

    
        elif amount<=self.loanlimit:
            loanFees=0.05*amount
            self.loan=amount+loanFees
            self.balance+=self.loan
            transaction1={'Borrow_Amount':amount,'New_balance':self.balance,'narration':"You got a  LOAN",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"You have recieved your loan of {amount}.You will be charged an interest of {loanFees} per month till you  finish paying.Your new acc balance is {self.balance}"
        

    def repay(self,amount):
        

            

            try:
                amount+10
            except TypeError:
                return f" please input amount in digits"    
            if amount<0:
                return f"You cannot repay with amount less than 0"
            elif amount==self.loan:
                return f" your loan of {self.loan} is fully paid"    
            elif self.loan>=amount:
                self.loan=self.loan-amount
                transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
                self.transactions.append(transaction1)
                return f"Your loan balance is {self.loan}"

            else:
                 
                amount >=self.loan
                remainder=amount-self.loan
                self.balance+=remainder
                transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
                self.transactions.append(transaction1)
                return f"{amount} has been used to repay your loan,the remainder has been added to your account and balance is {self.balance}"


            

            
    def get_statement(self):
            for items in self.transactions:
                amount=items['amount']
                balance=items['balance']
                narration=items["narration"]
                time=items['time']
                date=time.strftime("%D")
                print(f"On {date} {narration} {amount}.Balance:{balance}")


    def transfer(self,amount,account):
        try:
                amount+10
        except TypeError:
                return f" please input amount in digits" 

        fee=amount*0.05
        total=amount+fee
        new_balance=self.balance-total
        if self.balance<=0:
            return f"You have insufficient balance in your account to complete this transaction.Your current balance is{self.balance}"
        elif total>self.balance:
                return f"your balance is{self.balance} you need {total} to send {amount}"
        else:
            self.balance-=total
            account.deposit(amount)  
            transaction1={'Borrow_Amount':amount,'New_balance':self.balance,'narration':"You TRANSFERED",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"confirmed you have transfered KES {amount} to account{account.name} .your new balance is{new_balance}"      


class MobileMoneyAccount(Account):
    def __init__(self, name, phone,serviceProvider):
        Account.__init__( self,name,phone)
        self.serviceProvider=serviceProvider
    def buyAirtime(self,amount):

        try:
                amount+10
        except TypeError:
                return f" please input amount in digits" 
        if amount<=0:
            return f" your balance of {self.balance} below 0 .Top up & try again."
        elif amount<=self.balance:
            new_balance=self.balance-amount
            transaction1={'amount':amount,'New_balance':self.balance,'narration':"You BOUGHT AIRTIME",'time':datetime.now()}
            self.transactions.append(transaction1)
            
            return f"you have sucessfully bought  airtime worth {amount}.your new balance is {new_balance}"    

                
