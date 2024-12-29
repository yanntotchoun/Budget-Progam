import Person
import Income

class Goal:
    def __init__(self,name="",amount=0.0,percentage=0.0):#Constructor
        self.name = name
        self.amount = amount
        self.percentage = percentage
       

    def findGoal(self,goal,GoalList):#Find all of the financial goals for the user
       
      

        for i in range (goal):
            goalName = str(input('What is the name of this goal ?'))
            goalMoney = float(input(f'How much money do you want to save for this goal({goalName})?'))
            goal = Goal(goalName,goalMoney)
            GoalList.append(goal)

    def getSpecificGoalAmount(self,GoalList,goalSearch): #Find the amount of money for a specific goal(To be used with Money Allocation Class

        try:
            position  = GoalList.index(goalSearch)
        except ValueError:
            print(f"There is no goal with the name of {goalSearch}")

        goalTarget = GoalList[position].amount  

        return goalTarget
    

    def setSpecificPercentageForList(self,GoalList):#Method that will set the percentage of the Goal objects inside of the list

        length =len(GoalList)
        #i can a while here to make sure it's a 100 percent

        for i in range(length):
            goalPercentage = int(input(f"Please input a percentage in int for {GoalList[i].name} "))
            GoalList[i].percentage = goalPercentage
    

    def displayGoal(self,GoalList):# Method to display the financial Goals
        print(f"These are the financial goals for {Person.name}:")
        print()

        for goal in GoalList:
            print(goal.name)
            print()
            

    def timeTillGoal(self,goalSearch,GoalList,IncomeList):#Method that will find the time until we reach a specific goal
        

        goalFinalAmount = self.getSpecificGoalAmount(GoalList,goalSearch)

        monthlyIncome = Income.amountIncome(IncomeList)

        months = goalFinalAmount/monthlyIncome
        r_months = round(months,1)
        weeks = 4*r_months
        years = r_months/12

        print(f"To reach {goalFinalAmount} with a monthly income of {monthlyIncome} $, it would take you approximately {weeks} weeks, {r_months} months or {years} year(s)")


    def printMoneyAllocation(GoalList,IncomeList): # Will print what where to put the money that we allocate
        monthlyIncome = Income.amountIncome(IncomeList)
        length = len(GoalList)

        for i in range(length):

            print(f"For {GoalList[i].name}, you have allocated a percentage of {GoalList[i].percentage} so you should allocate {monthlyIncome}")
            print()




    

            
        


