import Person

person = Person()

class Income:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
        
        

    def findIncome(self,quantity,IncomeList):#Method for finding all of the Incomes source of a person
 
        for i in range (quantity):#Getting the information of the income, then creating an object an putting it inside of a list
            name = str(input(f'What is the name of the income{i} ?'))
            amount   = float(input(f'What is the amount of the income{i} ?'))
            IncomeObject = Income(name,amount)
            IncomeList.append(IncomeObject)

    def amountIncome(self,IncomeList):#Method to add the amount of the incomes together to the sum of incomes
        sumIncome =0
        for income in IncomeList:
            sumIncome +=  income.amount

        print(sumIncome)

    def displayIncome(self,IncomeList):# Method to display the incomes
        print(f"These are the source of income for {person.name}:")
        print()

        for income in IncomeList:
            print(income.name)
            print()


