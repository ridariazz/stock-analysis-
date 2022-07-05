# The data we need to retrieve 
# 1. The total number of votes cast
# 2. A compelete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 
# Import the datetime class from the datetime module
import datetime 
# Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
# Print the present time 
print("The time right now is, ", now)
import csv
dir(csv)
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file 
election_data = open(file_to_load, 'r')
# to do: perform analysis 

#close the file 
election_data.close()
# Open the election results and read the file 
with open(file_to_load) as election_data:
    # to do: perform analysis
    print(election_data)
import os
dir(os)
dir(os.path)
os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file 
with open(file_to_load) as election_data:
    # print the file object 
    print(election_data)
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode, we will write data to the file
open(file_to_save, "w")

# Using "with" statement to open the file as a text file
file_to_save = os.path.join("analysis", "election_analysis.txt")
txt_file = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies 
import csv
import os
#Open election_data file 
with open(file_to_load) as election_data:
    # to do: perform analysis
    print(election_data)
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    



    