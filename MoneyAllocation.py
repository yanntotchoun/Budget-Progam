import Goal
import Income
# I think this class is useless
class MoneyAllocation:
    def __init__(self):
        pass


    def timeTillGoal(self,goalSearch,GoalList,IncomeList):


        goalFinalAmount = Goal.getSpecificGoalAmount(GoalList,goalSearch)

        monthlyIncome = Income.amountIncome(IncomeList)

        months = goalFinalAmount/monthlyIncome
        r_months = round(months,1)
        weeks = 4*r_months
        years = r_months/12

        print(f"To reach {goalFinalAmount} with a monthly income of {monthlyIncome} $, it would take you approximately {weeks} weeks, {r_months} months or {years} year(s)")


    def printMoneyAllocation(GoalList,IncomeList):
        monthlyIncome = Income.amountIncome(IncomeList)
        length = len(GoalList)

        for i in range(length):

            print(f"For {GoalList[i].name}, you have allocated a percentage of {GoalList[i].percentage} so you should allocate {monthlyIncome}")
            print()

