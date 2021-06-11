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
        if amount <=0:
            print ("Enter a valid amount")
        else:
            self.balance=self.balance+amount
            transaction1={'amount':amount,'balance':self.balance,'narration':"You deposited",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"{self.name} you have deposited {amount} your new balance is {self.balance}"

   
   
    def widthdraw(self , amount)  :
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
            if amount<0:
                return f"You cannot repay with amount less than 0"
            elif amount >=self.loan:
                remainder=amount-self.loan
                self.balance+=remainder
                transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
                self.transactions.append(transaction1)
                return f"{amount} has been used to repay your loan,the remainder has been added to your account and balance is {self.balance}"
            else:
                 self.loan-=amount
            transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"Your loan balance is {self.loan}"


            
    def get_statement(self):
            for items in self.transactions:
                amount=items["amount"]
                balance=items['balance']
                narration=items["narration"]
                time=items['time']
                date=time.strftime("%D")
                print(f"On {date} {narration} {amount}.Balance:{balance}")