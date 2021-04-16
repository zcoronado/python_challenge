# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv 
import statistics 


filepath = os.path.join("..", 'Resources', 'budget_data.csv')
with open(filepath, 'r') as open_file: 
    csv_reader = csv.reader(open_file)

    next(csv_reader)

    dates = []
    profits = []
    profit_changes = []

    for row in csv_reader: 
        dates.append(row[0])
        if len(profits) > 0: 
            profit_changes.append(int(row[1])-profits[-1])
        profits.append(int(row[1]))
        

        #profit_loses = int(if budget_data[1] < 0)
       # profit_wins = int(if budget_data[1] > 0)
# The total number of months included in the dataset
    unique_date = len(dates) 
    print(unique_date)


# # The net total amount of "Profit/Losses" over the entire period

    total_net  =  sum(profits)
    print(total_net)


# # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    average_profits = round(statistics.mean(profit_changes),2)
    print(average_profits)

# # The greatest increase in profits (date and amount) over the entire period
#     greatest_increase = profit_wins.max()

# # The greatest decrease in losses (date and amount) over the entire period
#     greatest_decrease = profit_wins.min()

# # As an example, your analysis should look similar to the one below:

# #  ```text
# #  Financial Analysis
# #  ----------------------------
# #  Total Months: 86
# #  Total: $38382578
# #  Average  Change: $-2315.12
# #  Greatest Increase in Profits: Feb-2012 ($1926159)
# #  Greatest Decrease in Profits: Sep-2013 ($-2196167)
# #  ```
#      print(f'''
#         Financial Analysis
#         ===============================
#         Total Months : {round(unique_date, 2)}
#         Total :  {round(total_net, 2)}
#         Average  Change: ${round(, 2 )}
#         Greatest Increase in Profits: {greatest_increase}
#         Greatest Decrease in Profits: {greatest_decrease}
#     ''')


#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.