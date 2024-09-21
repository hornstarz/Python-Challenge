#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:22:22 2024

@author: zachhorn

""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
average_change = 0
greatest_increase = float('-inf')
greatest_decrease = float('inf')
previous_profit_loss = None
current_profit_loss = None
greatest_increase_date = ""
greatest_decrease_date = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    

   # Track the total and net change

    # Process each row of data
    for row in reader:
        total_months += 1
        current_profit_loss = int(row[1])
        
        # Track the total
        total_net += current_profit_loss

        # Track the net change
        profit_change = current_profit_loss - previous_profit_loss
        change = profit_change
        

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        # Calculate the greatest decrease in losses (month and amount)

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
        
        # I am updating the Previous profit loss for the next iteration    
        previous_profit_loss = current_profit_loss

# Calculate the average net change across the months
average_change = (total_net - int(first_row[1])) / (total_months - 1)

# Generate the output summary
output_summary = (f"Financial Analysis\n"
                  f"---------------------------\n"
                  f"Total Months: {total_months}\n"
                  f"Total: ${total_net}\n"
                  f"Average Change: ${average_change:.2f}\n"
                  f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
                  f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)


