# Import required modules
import os
import csv

# Store path to budget data csv
election_data_path = os.path.join('Resources', 'election_data.csv')

with open(election_data_path, newline='') as data_file:
    election_data = csv.reader(data_file, delimiter = ',')
    
    # Initialze variables
    vote_count = 0

    for row in election_data:
        # Increment vote counter
        vote_count += 1


report_dictionary = dict([
    ("Total Votes:", vote_count)
])


# Print report
os.system('clear')
# print(header)
for key, val in report_dictionary.items():
    print(key, val)
