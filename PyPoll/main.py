# Import required modules
import os
import csv

# Store path to budget data csv
election_data_path = os.path.join('Resources', 'election_data.csv')

with open(election_data_path, newline='') as data_file:
    election_data = csv.reader(data_file, delimiter = ',')
    header = next(election_data)
    
    # Initialze variables
    vote_count = 0
    election_dictionary = {}

    for row in election_data:
        # Increment vote counter
        vote_count += 1

        # Build election dictionary
        candidate = row[2]
        if candidate in election_dictionary:
            election_dictionary[candidate] += 1
        else:
            election_dictionary[candidate] = 1

# Determine winner
most_votes = 0
for key, val in election_dictionary.items():
    if val > most_votes:
        winner = key
        most_votes = val


# Set report formatting elements
header = "Election Results"
separator = "----------------------------"


# Print report
os.system('clear')
print(header)
print(separator)
print(f"Total Votes: {vote_count}")
print(separator)
for key, val in election_dictionary.items():
    percentage = round(val * 100 / vote_count)
    print(f"{key}: {percentage}% ({val})")
print(separator)
print(f"Winner: {winner}")
print()

# Write to file
f = open("Election_Report.txt","w",encoding="utf8")
f.writelines(f"{header}\n")
f.writelines(f"{separator}\n")
f.writelines(f"Total Votes: {vote_count}\n")
f.writelines(f"{separator}\n")
for key, val in election_dictionary.items():
    percentage = round(val * 100 / vote_count)
    f.writelines(f"{key}: {percentage}% ({val})\n")
f.writelines(f"{separator}\n")
f.writelines(f"Winner: {winner}")
f.close()
