# Programmers: Oreoluwa Adebusoye, Liv Oakes, Paige Ronan
# Course: CS151, Zelalem Yalew
# Due Date: 11/20
# Programming Assignment: Lab 10
# Problem Statement: analyze data on movies, their budgets, and their profits
# Data In: file name
# Data Out: table of movies with their profit and what movie had the highest profit
# Credits: class resources

import os

# Purpose: read file on to a table
# Parameters: filename
# Return: table
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



# Purpose: adding profit to table
# Parameters: table
# Return: table
def add_profit(table):
    for row in table:
        # Extract the budget and worldwide gross
        budget = row[2]
        domestic_gross = row[3]
        worldwide_gross = row[4]

        # Calculate the profit
        profit = (domestic_gross +worldwide_gross) - budget

        # Append the profit to the row
        row.append(profit)

    return table

# Purpose: to output the table
# Parameters: table and output_file
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

#def highest profit():


# Purpose:
# Parameters:
# Return:
def main():
    input_file = input("Enter the input CSV file name: ")
    while input_file != 'movies.csv':
        print("Please enter a valid CSV file.")
        input_file = input("Enter the input CSV file name: ")
    read_file(input_file)
    add_profit(read_file(input_file))
    write_list_to_file(read_file(input_file), input_file)
main()