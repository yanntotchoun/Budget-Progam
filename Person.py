class Person:
    def __init__(self,name= "",age="",moneySaved = 0,goal=0):#Constructor for the Person Class
        self.name =name
        self.age = age
        self.moneySaved = moneySaved
        self.goal= goal
   
      
    def displayPerson(self):
        print(f'The name of the user is {self.name}')
        print(f'The age of the user is {self.age}')
        print(f'{self.name} has {self.moneySaved}$ saved in his bank account')
        print(f'{self.name} has {self.goal} financial objectives')
    