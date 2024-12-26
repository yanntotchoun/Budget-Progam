
class Expense:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
     

    def findExpense(self,quantity):#Method for finding all of the Expenses of a person
        quantiy = int(input("How many sources of income do you have ?"))
        ExpenseList= []

        for i in range (quantity):#Getting the information of the Expense, then creating an object an putting it inside of a list
            name = str(input(f'What is the name of the income{i} ?'))
            amount   = float(input(f'What is the amount of the income{i} ?'))
            ExpenseObject = Expense(name,amount)
            ExpenseList.append(ExpenseObject)

    