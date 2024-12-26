import Person


class Income:
    def __init__(self,name=" ",amount=0,IncomeList=None):#Constructor for the Income Class
        self.name = name
        self.amount = amount
        if IncomeList is None:
            self.IncomeList = []
        else:
            self.IncomeList = IncomeList
        
        

    def findIncome(self,quantity,IncomeList):#Method for finding all of the Incomes source of a person
        quantity = int(input("How many sources of income do you have ?"))
  

        for i in range (quantity):#Getting the information of the income, then creating an object an putting it inside of a list
            name = str(input(f'What is the name of the income{i} ?'))
            amount   = float(input(f'What is the amount of the income{i} ?'))
            IncomeObject = Income(name,amount)
            IncomeList.append(IncomeObject)

    def amountIncome(self,IncomeList):#Method to add the amount of the incomes together to the sum of incomes
        sumIncome =0
        for income in IncomeList:
            sumIncome +=  income.amount
        print(f'{Person.name} has an income of {sumIncome} per month')

    def displayIncome(self,IncomeList):# Method to display the incomes
        print(f"These are the source of income for {Person.name}:")
        print()

        for income in IncomeList:
            print(income.name)
            print()


