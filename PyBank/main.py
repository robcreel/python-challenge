# Import required modules
import os
import csv

# Store path to budget data csv
budget_data_path = os.path.join('Resources', 'budget_data.csv')

# Function to update an ongoing average
def update_average(new_value, old_average, old_count):
    return (old_count * old_average + new_value)/(old_count + 1)

# Function to get row count
# Copied from https://stackoverflow.com/questions/970983/have-csv-reader-tell-when-it-is-on-the-last-line
def get_row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)

row_count = get_row_count(budget_data_path)

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
    total_delta = 0
    
    # Loop through the rows of data
    for row in budget_data:
        # Increment month counter
        month_count += 1

        # Get this month's profit
        profit_this_month = int(row[1])
        
        # Get first and last month's profit
        if month_count == 1:
            first_month_profit = profit_this_month
        
        if month_count == (row_count - 1):
            final_month_profit = profit_this_month

        # Calculate this month's profit delta
        delta_this_month = profit_this_month - profit_last_month

        # Update max increase or decrease if necessary.
        if delta_this_month > max_increase:
            max_increase = delta_this_month
            max_increase_month = row[0]
        if delta_this_month < max_decrease:
            max_decrease = delta_this_month
            max_decrease_month = row[0]

        # Update average change
        # print(f"delta this month: {delta_this_month}, average delta: {average_delta}, month count - 1: {month_count - 1}")
        # average_delta = update_average(delta_this_month, average_delta, month_count - 1)
        
        # Update total profit
        profit = profit + profit_this_month

        # Update profit profit_last_month in preparation for next loop
        profit_last_month = profit_this_month

        
# Calculate average change
average_delta = (final_month_profit - first_month_profit) / (row_count - 2)
average_delta = round(average_delta, 2)


# Build report
header = "Financial Analysis \n----------------------------"
report_list = [
    f"Total Months: {month_count}",
    f"Total: ${profit}",
    f"Average Change: ${average_delta}",
    f"Greatest Increase in Profits: {max_increase_month} ($ {max_increase})",
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"
]


# Print report
os.system('clear')
print(header)
for item in report_list:
    print(item)
print()

# Write to file
f = open("Financial_Analysis_Report.txt","w",encoding="utf8")
f.writelines(f"{header}\n")
for item in report_list:
    f.writelines(item + "\n")
f.close()
