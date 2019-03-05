import pandas as pd
import os
import csv

csvpath = ('/Users/HeatherTrinh/Desktop/RiceUDataAnalytics/PyBank/budget_data.csv')
budgetdata = pd.read_csv(csvpath)

# The total number of months included in the dataset
BankCount = budgetdata['Date'].count()
# The net total amount of "Profit/Losses" over the entire period
BankSum = '${:.0f}'.format(budgetdata['Profit/Losses'].sum())


#Determine the amount of increase or decrease from the previous month
AmtChange = budgetdata["Profit/Losses"].diff()
budgetdata["Amount Changed"] = AmtChange

# The greatest increase in profits (date and amount) over the entire period
BankMax = budgetdata.loc[budgetdata['Profit/Losses'].idxmax(), 'Date']
GreatestIncrease = '${:.0f}'.format(budgetdata["Amount Changed"].max())

# The greatest decrease in losses (date and amount) over the entire period
BankMin = budgetdata.loc[budgetdata['Profit/Losses'].idxmin(), 'Date']
GreatestDecrease = '${:.0f}'.format(budgetdata["Amount Changed"].min())

# The average of the changes in "Profit/Losses" over the entire
BankAvg = '${:.2f}'.format(budgetdata["Amount Changed"].mean())

print('Total Months:')
print(BankCount)
print('Total:')
print(BankSum)
print('Average Change:')
print(BankAvg)
print('Greatest Increase in Profits:')
print(BankMax)
print(GreatestIncrease)
print('Greatest Decrease in Profits:')
print(BankMin)
print(GreatestDecrease)