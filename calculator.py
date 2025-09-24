# September 09 2025 3:58 pm EST
# Author: Logan B Seeley
# Description: This program is a calculator for deterrmining total expenses based on income and expenses
# version 2.0.0
# License: 

import Functions


print ("welcome to my budgeting software \n we are going to ask you questions about things like income, debt, savings and any expendatures you have to find out how to takle your debt and to get your savings up. \n let's start with your income this month \n")
Functions.INCOME_this_month(1)

print (" now how much debt do you have?\n")
Functions.how_much_debt(2)

print ("time for your rent or mortgage?\n")
Functions.rent_this_month(3)

print (" now its time for your bill for utilities and services \n")
Functions.utilities_this_month(4)

print (" how much did you spend on groceries?\n")
Functions.groceries_this_month(5)

print (" now we are going to tackle your subscriptions, cell plan and other recurring payments?\n")
Functions.subscriptions_this_month(6)

print (" what did you spend on your wants not your needs?\n")
Functions.entertainment_this_month(7)

print (" now lets find out your goal for your savings\n")
Functions.savings_goal(8)

print (" now to tackle the debt\n")
Functions.debt_payoff_plan(9,2)

print (" finally lets get a summary of your month\n")
Functions.final_summary(1,2,3,4,5,6,7,8,9)
print (" thank you for using my budgeting software\n have a wonderfull day! :)")

