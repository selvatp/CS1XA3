## Program for an Accountant
## budget.py
#By: Piranaven Selvathayabaran


## PROGRAM RUNS  BY ADDING EXPENSE AND REVENUE ONE BY ONE : TO STOP, TYPE :0

class Budget:

    def __init__(self,balance):
        self.initial=balance
        self.month_revenue=[]
        self.month_expense=[]


    def setBalance(self):
        self.balance=self.initial
        return self.balance 
        

    def addMonth(self,ramount, eamount):
        self.month_revenue.append(ramount)
        self.month_expense.append(eamount)

    def getLists(self):
        tr=self.balance
        te=0
        for i in range(len((self.month_revenue))):
            tr=tr+ int(self.month_revenue[i])
        for i in range(len(self.month_expense)):
            te=te+ int(self.month_expense[i])

        
        self.tr=tr
        self.te=te

        print("The total revenue minus the total expense for the whole budget:"+str(self.tr-self.te))

  
        
        

def main():

    print("This program calculates the total revenue minus the total expense for the whole budget: ")
    print()
    balance=eval(input ("Please enter the initial balance: "))
    x = Budget(balance)
    x.setBalance()
    print()
    revenue=0
    while revenue != "x":

        print("Enter 0 into revenue when you would like to end")
        print()
        revenue=eval(input("Enter a revenue this month: "))
        if revenue == 0:
            break
        expense =eval(input("Enter the expense this month: "))
        x.addMonth(revenue,expense)
        print()

    x.getLists()

    
    
    


if __name__ == '__main__': main()        
