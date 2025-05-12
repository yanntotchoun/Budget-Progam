import Person
import json

class Expense:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
    

    def findExpense(self,quantity,ExpenseList):#Method for finding all of the Expenses of a person
        
        for i in range (quantity):#Getting the information of the Expense, then creating an object an putting it inside of a list
            self.name = str(input('What is the name of the expense ?'))
            self.amount   = float(input(f'What is the amount of the expense named {self.name} ?'))
            ExpenseDict = {"name":self.name,"amount":self.amount}
            ExpenseList.append(ExpenseDict)
            with open("expense.json","w") as file:
                json.dump(ExpenseList,file,indent =4)

    def amountExpense(self,ExpenseList):#Method to add the amount of the expenses together to the sum of expenses
        sumExpense = 0
        for expense in ExpenseList:
            sumExpense += expense.amount

        return sumExpense

    def displayExpense(self,ExpenseList,user):# Method to display the expenses
        print(f"These are the expenses for {user.name}:")
        print()

        for expense in ExpenseList:
            print(expense.name)
            print(expense.amount)
#This from_dict method takes a dictionary like {"name": "Job", "amount": 2000} and creates an Income object from it.
def from_dict(cls, data):
        return cls(data['name'], data['amount'])


    