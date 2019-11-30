# Import required modules
import os
import csv

# Store path to budget data csv
budget_data_path = os.path.join('Resources', 'budget_data.csv')

# Function to update an ongoing average
def update_average(new_value, old_average, old_count):
    return (old_count * old_average + new_value)/(old_count + 1)

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
    average_delta = 0
    
    # Loop through the rows of data
    for row in budget_data:
        # Increment month counter
        month_count += 1

        # Get this month's profit
        profit_this_month = int(row[1])

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
        print(f"delta this month: {delta_this_month}, average delta: {average_delta}, month count - 1: {month_count - 1}")
        average_delta = update_average(delta_this_month, average_delta, month_count - 1)
        
        # Update total profit
        profit = profit + profit_this_month

        # Update profit profit_last_month in preparation for next loop
        profit_last_month = profit_this_month


# Build report
header = "Financial Analysis \n----------------------------"
report_dictionary = dict([
    ("Total Months:", month_count),
    ("Total:", profit),
    ("Average Change:", average_delta),
    ("Greatest Increase in Profits: ", max_increase),
    ("Greatest Decrease in Profits:", max_decrease)
])


# Print report
# os.system('clear')
print(header)
for key, val in report_dictionary.items():
    print(key, val)

# Write to file
f = open("report.txt","w",encoding="utf8")
f.writelines(f"{header}\n")
for key, val in report_dictionary.items():
    f.writelines(f"{key} {val}\n")
f.close()
