#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:23:09 2024

@author: zachhorn
"""
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = ["Chalres Casper Stockham", "Diana DeGette", "Ramon Anthony Doane"]
vote_percent = ""
total_votes_won = 0

# Define lists and dictionaries to track candidate names and vote counts
vote_count = {"Charles Casper Stockham": 0, "Diana DeGette": 0,"Raymon Anthony Doane": 0}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]
       
        # If the candidate is not already in the candidate list, add them
        if candidate_name in vote_count:

        # Add a vote to the candidate's count
            vote_count[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Election Results\n")
    print(f"-------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print(f"-------------------\n")

    # Write the total vote count to the text file (I also added some additional lines for formatting as well)
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------\n")

    

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in vote_count.items():
    
        # Get the vote count and calculate the percentage
        vote_percent = (votes / total_votes) *100
        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percent:.3f}% ({votes})\n")
        txt_file.write(f"{candidate}: {vote_percent:.3f}% ({votes})\n")
  
        

    # Generate and print the winning candidate summary
    print(f"-------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print(f"-------------------\n")

    # Save the winning candidate summary to the text file
    txt_file.write(f"-------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"-------------------\n")