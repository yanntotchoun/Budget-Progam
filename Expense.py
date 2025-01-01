import Person

class Expense:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
    

    def findExpense(self,quantity,ExpenseList):#Method for finding all of the Expenses of a person
        
        for i in range (quantity):#Getting the information of the Expense, then creating an object an putting it inside of a list
            name = str(input('What is the name of the expense ?'))
            amount   = float(input(f'What is the amount of the expense named {name} ?'))
            ExpenseObject = Expense(name,amount)
            ExpenseList.append(ExpenseObject)

    def amountExpense(self,ExpenseList):#Method to add the amount of the expenses together to the sum of expenses
        sumExpense = 0
        for expense in ExpenseList:
            sumExpense +=  expense.amount

        return sumExpense

    def displayExpense(self,ExpenseList,user):# Method to display the expenses
        print(f"These are the expenses for {user.name}:")
        print()

        for income in ExpenseList:
            print(income.name)
            print()



    