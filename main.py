# Programmers: Oreoluwa Adebusoye, Liv Oakes, Paige
# Course: CS151, Zelalem Yalew
# Due Date: 11/20
# Programming Assignment: Lab 10
# Problem Statement:
# Data In:
# Data Out:
# Credits:

import os

# Purpose:
# Name:
# Parameters:
# Return:
def read_file(filename):
    table = []

    try:
        file = open(filename, "r")
        for line in file:
            # Split the line by commas to create a list row
            row = line.strip().split(',')
            row[2] = int(row[2])  # Convert Movie budget to integer
            row[3] = int(row[3])  # Convert domestic gross to integer
            row[4] = int(row[4])  # Convert Worldwide Gross

            # Append the row to the table
            table.append(row)

        file.close()  # Close the file after reading

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")

    return table



# Purpose:
# Name:
# Parameters:
# Return:
def add_profit(table):
    for row in table:
        # Extract the budget and worldwide gross
        budget = row[2]
        worldwide_gross = row[4]

        # Calculate the profit
        profit = worldwide_gross - budget

        # Append the profit to the row
        row.append(profit)

    return table

# Purpose:
# Name:
# Parameters:
# Return:
def write_list_to_file(table, output_file):
    # Open the file for writing
    fd = open(output_file, "a")

    for row in table:
        # Initialize an empty string for the line
        line = ''

        # Loop through each item in the row and concatenate to line
        for item in row:
            line += str(item) + ','

        # Remove the trailing comma from the line
        line = line.rstrip(',')

         # Write the line to the output file followed by a newline
        output_file.write(line + '\n')
    # Close the file
    fd.close()

    print(f"Data successfully written to '{output_file}'.")

# Purpose:
# Name:
# Parameters:
# Return:
def main():
    input_file = input("Enter the input CSV file name: ")