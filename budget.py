#Getting all of the variables to initialise my objects
ame = str(input('What is your name ?'))
age = int(input('What is your name ?'))
moneySaved = float(input('How much money do you have saved currently ?'))
goal = int(input('How many financial goals do you have'))
incomeName =str(input('What is/are your monthly income(s)?'))
ExpenseName = str(input("What are your monthly expenses"))
income = float(input('What is the sum your monthly income ?'))
expense = float(input('What is the sum of your your name ?'))


'''
Ne pas oublier de tester à chaque pour assurer que tous run sans problème

'''


class Person:
    def __init__(self,name= "",age="",moneySaved = 0,income=0,expense=0):#Constructor for the Person Class
        self.name =name
        self.age = age
        self.moneySaved = moneySaved
        self.goal= goal
        self.income =income
        self.expense =expense
      
    def displayPerson(self):
        print(f'The name of the user is {self.name}')
        print(f'The age of the user is {self.age}')
        print(f'{self.name} has {self.moneySaved}$ saved in his bank account')
        print(f'{self.name} has {self.goal} financial objectives')
        print(f'{self.name} loses {self.expense}')


class Income:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
        

    def findIncome(self):#Method for finding all of the Incomes source of a person
        quantiy = int(input("How many sources of income do you have ?"))
        incomeList= []

        for i in range (quantiy):#Getting the information of the income, then creating an object an putting it inside of a list
            name = str(input(f'What is the name of the income{i} ?'))
            amount   = float(input(f'What is the amount of the income{i} ?'))
            income = Income(name,amount)
            incomeList.append(income)










