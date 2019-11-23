# Import required modules
import os
import csv

# Store path to budget data csv
budget_data_path = os.path.join('Resources', 'budget_data.csv')

# Open file and conduct analysis
with open(budget_data_path, newline='') as data_file:
    budget_data = csv.reader(data_file, delimiter = ',')
    header = next(budget_data)

    # Initialze the month count at negative rather than zero
    # to exclude the header from counting as a month
    month_count = 0

    # Initialize profit/loss at zero
    profit = 0
    profit_this_month = 0
    
    # Loop through the rows of data
    for row in budget_data:
        # print(f"{row[1]}")
        # Increment month counter
        month_count += 1
        profit_this_month = int(row[1])

        # Update total profit
        profit = profit + profit_this_month


# Print report
os.system('clear')
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: ${profit}")

    # header = next(budget_data)
    # print(f"Header: {header}")
    # line1 = next(budget_data)
    # print(f"Line 1: {line1}")
    # line2 = next(budget_data)
    # print(f"Line 2: {line2}")