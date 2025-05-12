import Person
import json


class Income:
    def __init__(self,name=" ",amount=0):#Constructor for the Income Class
        self.name = name
        self.amount = amount
        
       

    def findIncome(self,quantity,IncomeList):#Method for finding all of the Incomes source of a person
  
        for i in range (quantity):#Getting the information of the income, then creating an object and putting it inside of a list
            #Initialising data members
            self.name = str(input('What is the name of the income ?'))
            self.amount   = float(input(f'What is the amount of the income named {self.name} ?'))
            #Creating an Income Object
            IncomeObject = Income(self.name,self.amount)
            #Converting the Income Object into a dictionnary
            IncomeDict = {"name":self.name,
                          "amount":self.amount
            }
            #Adding the Objects(Dictionnaries) into a list
            IncomeList.append(IncomeDict)
            #Opening the file to read it
            with open("income.json",'w') as file:
                #Adding the list into the json file
                json.dump(IncomeList,file,indent =4)


     

    def amountIncome(self,IncomeList):#Method to add the amount of the incomes together to the sum of incomes
        sumIncome =0
        for income in IncomeList:
            #since it is a dictionary, I have to use a different way such as income["name"]. In this situation, income is the name of the object inside of the IncomeList list
            sumIncome += income.amount
        return sumIncome

    def displayIncome(self,IncomeList,user):# Method to display the incomes
        
        print(f"These are the source of income for {user.name}:")
        print()

        for income in IncomeList:
            print(income.name)
            print(income.amount)

#This from_dict method takes a dictionary like {"name": "Job", "amount": 2000} and creates an Income object from it.
def from_dict(cls, data):
        return cls(data['name'], data['amount'])