# September 09 2025 3:36 pm EST
# Author: Logan B Seeley
# Description: This project is to manage personal expenses, income and debt 
# version 1.2.0
# License: 

# collecting data from user
def INCOME_this_month(income):
    print ("what was your income this month?") 
    income = input()
    print ("Confirm your income this month was: " + income)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Income confirmed.")
    else:
        print ("what was your income this month?")
        income = input()
        print ("Confirm your income this month was: " + income)
        confirm = input("y/n: ")
(INCOME_this_month)

def subscriptions_this_month(sub):
    print ("what were your subscriptions cost this month? all together")
    sub = input()
    print ("Confirm your subscriptions cost this month were: " + sub)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Subscriptions cost confirmed.")
    else:
        print ("what were your subscriptions cost this month? all together")
        sub = input()
        print ("Confirm your subscriptions cost this month were: " + sub)
        confirm = input("y/n: ")
(subscriptions_this_month)

def groceries_this_month(groceries):
    print ("what were your groceries cost this month? all together")
    groceries = input()
    print ("Confirm your groceries cost this month were: " + groceries)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Groceries cost confirmed.")
    else:
        print ("what were your groceries cost this month? all together")
        groceries = input()
        print ("Confirm your groceries cost this month were: " + groceries)
        confirm = input("y/n: ")
(groceries_this_month)

def rent_this_month(rent):
    print ("what was your rent this month?")
    rent = input()
    print ("Confirm your rent this month was: " + rent)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Rent confirmed.")
    else:
        print ("what was your rent this month?")
        rent = input()
        print ("Confirm your rent this month was: " + rent)
        confirm = input("y/n: ")
(rent_this_month)

def utilities_this_month(utilities):
    print ("what were your utilities cost this month? all together")
    utilities = input()
    print ("Confirm your utilities cost this month were: " + utilities)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Utilities cost confirmed.")
    else:
        print ("what were your utilities cost this month? all together")
        utilities = input()
        print ("Confirm your utilities cost this month were: " + utilities)
        confirm = input("y/n: ")
(utilities_this_month)

def entertainment_this_month(other):
    print ("how much did you spend on yourself for things like hobbies and fun this month? all together")
    other = input()
    print ("Confirm the cost this month were: " + other)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Entertainment cost confirmed.")
    else:
        print ("how much did you spend on yourself for things like hobbies and fun this month? all together")
        other = input()
        print ("Confirm your entertainment cost this month were: " + other)
        confirm = input("y/n: ")
(entertainment_this_month)

def summary(income, sub, groceries, rent, utilities, other):
    total_expenses = float(sub) + float(groceries) + float(rent) + float(utilities) + float(other)
    net_income = float(income) - total_expenses
    print ("Your total expenses this month were: " + str(total_expenses))
    print ("Your net income this month is: " + str(net_income))
(summary)

def savings_goal(savings_goal):
    print (" how much do you want to save this month? ")
    savings_goal = input()
    print ("Confirm your savings goal this month is: " + savings_goal)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Savings goal confirmed.")
    else:
        print (" how much do you want to save this month? ")
        savings_goal = input()
        print ("Confirm your savings goal this month is: " + savings_goal)
        confirm = input("y/n: ")
(savings_goal)

def how_much_debt(debt):
    print ("in dollars what is your total debt?")
    debt = input()
    print ("Confirm your total debt is: " + debt)
    confirm = input("y/n: ")
    if confirm == "y":
        print ("Debt confirmed.")
    else:
        print ("how much debt do you have? all together")
        debt = input()
        print ("Confirm your total debt is: " + debt)
        confirm = input("y/n: ")
(how_much_debt)

def debt_payoff_plan(debt_payment, income):
    print ("how much of your income do you want to put towards debt each month?")
    perc = input()
    debt_payment = ((int(income)/100 ) * int(perc))
    print ("Confirm your debt payment plan is: " + debt_payment)
    if confirm == "y":
        print ("Debt payment plan confirmed.")
    else:
        print ("how much of your income do you want to put towards debt each month?")
        perc = input()
        debt_payment = ((int(income)/100 ) * int(perc))
        print ("Confirm your debt payment plan is: " + debt_payment)
        confirm = input("y/n: ")
(debt_payoff_plan)

def final_summary(summary_of_expense, income, savings_goal, debt_payment):
    total_expenses = float(summary_of_expense) + float(debt_payment) + float(savings_goal)
    net_income = float(income) - total_expenses
    print ("Your total expenses this month were: " + str(total_expenses))
    print ("Your net income this month is: " + str(net_income))
(final_summary)

def summary_of_expense(income, sub, groceries, rent, utilities, other):
    total_expenses = int(sub) + int(groceries) + int(rent) + int(utilities) + int(other)
    print ("Your total expenses this month are: " + str(total_expenses))
    remaining_income = int(income) - int(total_expenses)
    print ("Your total income after expenses is: " + str(remaining_income))
(summary_of_expense)

def summary_of_savings(savings, remaining_income, summary_of_expense):
    potential_savings =  int(remaining_income) - int(summary_of_expense)
    print ("Your potential savings after this month is: " + str(potential_savings))
    print (" how much in a pertentage of your remaining income would you like to save?") 
    perc = int(input())
    savings = (int(remaining_income)/100 ) * int(perc)
    print (" you total savings this month is: " + str(savings))
(summary_of_savings)

def future_pay(income,savings, debt_payment, summary_of_expense):
    total_expenses = int(summary_of_expense) + int(debt_payment) + int(savings)
    net_income = int(income) - total_expenses
    print ("Your total expenses next month will be: " + str(total_expenses))
    print ("Your net income next month will be: " + str(net_income))
(future_pay)

