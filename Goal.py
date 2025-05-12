import Person
import Income
import json

class Goal:
    def __init__(self,name="",amount=0,percentage=0.0):#Constructor
        self.name = name
        self.amount = amount
        self.percentage = percentage
    
       

    def findGoal(self,quantity,GoalList):#Find all of the financial goals for the user
       
      

        for i in range (quantity):
            goalName = str(input('What is the name of this goal ?'))
            goalMoney = float(input(f'How much money do you want to save for this goal({goalName})?'))
            goal = Goal(goalName,goalMoney)
            goal_dict = {"name":goalName,"amount":goalMoney,"percentage":0}
            GoalList.append(goal_dict)
            with open("goal.json","w") as file:
                json.dump(GoalList,file,indent=4)


    def getSpecificGoalAmount(self,GoalList): #Find the amount of money for a specific goal(To be used with Money Allocation Class
        position =-1
        goalSearch =0
        for i, goal in enumerate(GoalList):
            if goal["name"] == goalSearch:  
                position = i
                break
            else:
             print(f"{goalSearch} is not in one of your financial goals.")


        
        if position <0:
             goalTarget = -1
        else:
            goalTarget = GoalList[position].amount

        return goalTarget
    

    def setSpecificPercentageForList(self,GoalList):#Method that will set the percentage of the Goal objects inside of the list

        length =len(GoalList)
        #i can put a while here to make sure it's a 100 percent

        for i in range(length):
            goalPercentage = int(input(f"Please input a number for percentage for {GoalList[i].name}"))
            goalPercentage /= 100
            GoalList[i].percentage = goalPercentage
    

    def displayGoal(self,GoalList,user):# Method to display the financial Goals
        print(f"These are the financial goals for {user.name}:")
        print()

        for goal in GoalList:
            print(goal.name)
            print(goal.amount)
            

    def timeTillGoal(self,goalSearch,GoalList,IncomeList,income):#Method that will find the time until we reach a specific goal
        

        goalFinalAmount = self.getSpecificGoalAmount(GoalList,goalSearch)

        if goalFinalAmount > 0:
            monthlyIncome = income.amountIncome(IncomeList)
            months = goalFinalAmount/monthlyIncome
            r_months = round(months,1)
            weeks = 4*r_months
            years = r_months/12
            print(f"To reach {goalFinalAmount} for your {goalSearch} goal with a monthly income of {monthlyIncome} $, it would take you approximately {weeks} weeks, {r_months} months or {years} year(s)")
        else:
            print(f"{goalSearch} is not in one of your financial goals.")

    def printMoneyAllocation(self,GoalList,IncomeList,income): # Will print what where to put the money that we allocate
        monthlyIncome = income.amountIncome(IncomeList)
        length = len(GoalList)

        for i in range(length):

            print(f"For {GoalList[i].name}, you have allocated a percentage of {GoalList[i].percentage} so you should allocate {round(monthlyIncome*GoalList[i].percentage,2)}$ of your {monthlyIncome}$ monthly Income")
            print()




    
#This from_dict method takes a dictionary like {"name": "Job", "amount": 2000} and creates an Income object from it.
def from_dict(cls, data):
        return cls(data['name'], data['amount'])
            
        


