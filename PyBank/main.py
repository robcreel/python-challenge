# Import required modules
import os
import csv

# Store path to budget data csv
budget_data_path = os.path.join('Resources', 'budget_data.csv')

# Open file and conduct analysis
with open(budget_data_path, newline='') as data_file:
    budget_data = csv.reader(data_file, delimiter = ',')
    header = next(budget_data)

    # Initialze variables
    month_count = 0
    profit = 0
    profit_last_month = 0
    max_increase = 0
    max_decrease = 0
    
    # Loop through the rows of data
    for row in budget_data:
        # print(f"{row[1]}")
        # Increment month counter
        month_count += 1

        # Get this month's profit
        profit_this_month = int(row[1])

        # Calculate this month's profit delta
        delta_this_month = profit_this_month - profit_last_month

        # Update max increase or decrease if necessary.
        if delta_this_month > max_increase:
            max_increase = delta_this_month
            max_increase_row = row
        if delta_this_month < max_decrease:
            max_decrease = delta_this_month
            max_decrease_row = row
        
        # Update total profit
        profit = profit + profit_this_month


# Print report
os.system('clear')
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: ${profit}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: {max_increase_row[0]} ($ {max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_row[0]} (${max_decrease})")

# TODO: According to answer key, my max increase and decrease months are correct, but not their values.  Fix this.