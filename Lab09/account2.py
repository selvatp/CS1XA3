## Program for an Accountant
## budget.py
#By: Piranaven Selvathayabaran


## PROGRAM RUNS  BY ADDING EXPENSE AND REVENUE ONE BY ONE : TO STOP, TYPE :0

class Budget:

    def __init__(self,):
        self.initial=0
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

    revenue =[]
    expense=[]
    infileName = input("What file are the budgets in ?")
    infile= open(infileName,'r')
    tr=0
    te=0
    for line in infile:
        x,y=line.split()
        revenue.append(x)
        expense.append(y)
        

    for i in range(len((revenue))):
        tr=tr+ int(revenue[i])
    for i in range(len(expense)):
        te=te+ int(expense[i])

    print("The budget for the first half is : " + str(tr-te))
        
    


if __name__ == '__main__': main()       
