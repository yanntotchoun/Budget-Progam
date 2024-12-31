#Getting all of the variables to initialise my objects
import Person
import Expense
import Income
import Goal

''''
Ne pas oublier de tester à chaque pour assurer que tous run sans problème

'''


GoalList =[]
ExpenseList = []
IncomeList = []

#Information to create the Person Class
print("Hello, this is a program to calculate your monthly budget.")
name = str(input('What is your name ?'))
age = int(input('What is your age ?'))
moneySaved = float(input('How much money do you have saved currently ?'))



#Person Object
user = Person.Person(name,age,moneySaved)

#Setting the income
print("First you need to set your Income(s).")
quantity = int(input("How many sources of income do you have ?"))
income = Income.Income()
income.findIncome(quantity,IncomeList)

#Setting the Expenses
print("Then you need to set your Expenses.")
quantity = int(input("How many expenses do you have ?"))
expense = Expense.Expense()
expense.findExpense(quantity,ExpenseList)

#Setting your Goal(s)
print("Lastly you'll need to set your financial goals if you have any.")
quantity = int(input("How many financial goals do you have ?"))
goal = Goal.Goal(income,expense)
goal.findGoal(quantity,GoalList)
''''

print(IncomeList)
print(ExpenseList)
print(GoalList)
'''


operation = int(input("What operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))
print()





while(operation != 6):

    if operation == 1:
        income.displayIncome(IncomeList,user)
        print(f"Your monthly income is {income.amountIncome(IncomeList)}")
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 2:
        expense.displayExpense(ExpenseList,user)
        print(f"The amount of your monthly expenses is {expense.amountExpense(ExpenseList)}")
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 3:
        goal.displayGoal(GoalList,user)
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 4:
        goal.setSpecificPercentageForList(GoalList)
        goal.printMoneyAllocation(GoalList,IncomeList)
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 5:
        goalSearch = str(input("What goal do you want to get a timeframe of ?"))
        goal.TimeTillGoal(goalSearch,GoalList,IncomeList)
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 6:
        print("You have successfully ended the program")
    else:
        print("Wrong Input. Try Again !")
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))


















