# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The Percentage of votes each candidate won
# 4. The total numver of votes each candidate won
# 5. The winner of the elcetion based on popular vote

import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save,"w")
# txt_file = open(file_to_save, "w")

# Write three counties to the file.
# txt_file.write ("Counties in the Election\n----------------\nJefferson\nDenver\nArapahoe")
# txt_file.write ("--------------------------")
# txt_file.write("Arapahoe")
# txt_file.write("Denver")
# txt_file.write("Jefferson")

#txt_file.write("Jefferson\Denver\Arapahoe")
# write some data to the file.
#outfile.write("Hello World")


with open(file_to_save, "w") as txt_file:

    # write some data tot he file.
    #text_file.write("Hello World")

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources\election_results.csv'

    file_to_load = os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    # To do: perform analysis.
    # To read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    #for row in file_reader:
        # print(row)
        # print(row[0])

    # Print the header row.
    headers = next(file_reader)
    print(headers)
  
    #print(election_data)
#Close the file.
#election_data.close()
# outfile.close()
    txt_file.close()