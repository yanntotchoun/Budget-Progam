#Getting all of the variables to initialise my objects
import Person
import Expense
import Income
import Goal
import json




''''
Ne pas oublier de tester à chaque pour assurer que tous run sans problème

'''


GoalList =[]
ExpenseList = []
IncomeList = []

#Information to create the Person Class 
user = Person.Person()
answer = str(input('Have you already logged in ? (Y or N)'))

if answer== 'y' or answer =="Y":
    #will open the json file named Person and read what is inside
    with open("person.json","r") as file:

        #Will save the json file as a dictionary
        person =json.load(file)

        #initialise the user object with keys inside of the json file
        user.setUserData(person["name"],person["age"],person["moneySaved"])
else:
    #will open the json file named Person and write inside
    with open("person.json","w") as file:
        #will run the getUserDataFunction 
        user.getUserData()
        
#Creating a Person object


#Setting the Income
print("First you need to set your Income(s).")
quantity = int(input('How many incomes do you currently have'))
income = Income.Income()

if answer=='y' or answer=='Y':
    with open("income.json","r") as file:
        data_list = json.load(file)
        income_object = [Income.from_dict(d)for d in data_list]
        #Instead of adding the entire list inside of the Income list with append , you use extend to add each objects individually
        IncomeList.extend(income_object)

    

else:
    with open("income.json","w") as file:
     income.findIncome(quantity,IncomeList)

#Setting the Expenses
print("Then you need to set your Expenses.")
quantity = int(input("How many expenses do you have ?"))
expense = Expense.Expense()
expense.findExpense(quantity,ExpenseList)

#Setting your Goal(s)
print("Lastly you'll need to set your financial goals if you have any.")
quantity = int(input("How many financial goals do you have ?"))
goal = Goal.Goal()
goal.findGoal(quantity,GoalList)




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
        goal.printMoneyAllocation(GoalList,IncomeList,income)
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 5:
        goalSearch = str(input("What goal do you want to get a timeframe of ?"))
        goal.timeTillGoal(goalSearch,GoalList,IncomeList,income)
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))

    elif operation == 6:
        print("You have successfully ended the program")
    else:
        print("Wrong Input. Try Again !")
        operation = int(input("What other operation do you want to do today.\n1. See your monthly Income\n2. See your your monthly expenses\n3. See your financial goals\n4. Allocate your money\n5. See how the time until you reach a certain financial goal.\n6. Exit Program "))


















