import json

class Person:
    def __init__(self,name= "",age="",moneySaved = 0):#Constructor for the Person Class
        self.name =name
        self.age = age
        self.moneySaved = moneySaved
   
      
    def displayPerson(self):
        print(f'The name of the user is {self.name}')
        print(f'The age of the user is {self.age}')
        print(f'{self.name} has {self.moneySaved}$ saved in his bank account')
     
    def getUserData(self):
        print("Hello, this is a program to calculate your monthly budget.")
        self.name = str(input('What is your name ?'))
        self.age = int(input('What is your age ?'))
        self.moneySaved = float(input('How much money do you have saved currently ?'))

        person = {
        "name":self.name,
        "age":self.age,
        "moneySaved":self.moneySaved
                }
        
        with open("person.json","w") as file:
            json.dump(person,file, indent=4)
    
    def setUserData(self,n,a,mS):
            self.name = n
            self.age = a
            self.moneySaved = mS

        

    