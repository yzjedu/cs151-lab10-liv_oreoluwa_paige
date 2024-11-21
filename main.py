# Programmers: Oreoluwa Adebusoye, Liv Oakes, Paige Ronan
# Course: CS151, Zelalem Yalew
# Due Date: 11/20
# Programming Assignment: Lab 10
# Problem Statement: This program analyzes data on movies, their budgets, and their profits.
#                    It calculates the profit for each movie, saves the updated data to a file,
#                     and identifies the movie with the highest profit.
# Data In: File name provided by the user (CSV file with movie data)
# Data Out: A table of movies with their profit and Information about the movie with the highest profit displayed to the user.
# Credits: class resources

import os

# Purpose: Read movie data from a CSV file and store it in a list of lists (table).
# Name: read_file
# Parameters: None (prompts user for file name)
# Return: table (list of lists)
def read_file():
    # Prompt user for the filename to read
    file_name = input("What file do you want to read? ")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(file_name):
        print("That file does not exist. Please try again.")
        file_name = input("\nWhat file do you want to read? ")

    # Initialize an empty list to store the movie data table
    table = []

    try:
        # Open the file for reading
        with open(file_name, "r") as file:
            for line in file:
                # Split the line by commas to create a list row
                row = line.strip().split(',')
                row[2] = int(row[2])  # Convert Movie Budget to integer
                row[3] = int(row[3])  # Convert Domestic Gross to integer
                row[4] = int(row[4])  # Convert Worldwide Gross to integer

                # Append the row to the table
                table.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")

    return table


# Purpose: Update the table by adding a column to hold the profit.
# Name: profit_column
# Parameters: table (list of lists)
# Return: The updated table with an additional profit column.
def profit_column(table):
    # Iterate through each row in the table
    for row in table:

        # Extract the budget and worldwide gross
        budget = row[2]
        worldwide_gross = row[4]

        # Calculate the profit
        profit = worldwide_gross - budget

        # Append the profit to the row
        row.append(profit)

    return table

# Purpose: Write the updated table with the profit column to a new CSV file.
# Name: write_list_to_file
# Parameters: table (list of lists), output_file
# Return: None
def write_list_to_file(table, output_file):
    # Open the output file for writing
    fd = open(output_file, "w")

    for row in table:
        # Initialize an empty string for the line
        line = ''

        # Loop through each item in the row and concatenate to line
        for item in row:
            line += str(item) + ','

        # Remove the trailing comma from the line
        line = line.rstrip(',')

        # Write the line to the output file followed by a newline
        fd.write(line + '\n')

    # Close the file
    fd.close()

    print(f"\nData successfully written to '{output_file}'.")

# Purpose: Find and display the movie with the highest profit.
# Name: highest_profit_movie
# Parameters: table (list of lists)
# Return: None
def highest_profit_movie(table):
    # Initialize with the first movie's profit
    max_profit_movie = table[0]
    max_profit = max_profit_movie[-1]  # The first movie's profit

    # Iterate through the table to find the movie with the highest profit
    for row in table:
        profit = row[-1]  # Profit is the last column in the row
        if profit > max_profit:
            max_profit = profit
            max_profit_movie = row

    # Display the details of the movie with the highest profit
    print("\nMovie with the highest profit:")
    print(f"Release Date: {max_profit_movie[0]}")
    print(f"Title: {max_profit_movie[1]}")
    print(f"Budget: ${max_profit_movie[2]:,d}")
    print(f"Domestic Gross: ${max_profit_movie[3]:,d}")
    print(f"Worldwide Gross: ${max_profit_movie[4]:,d}")
    print(f"Profit: ${max_profit_movie[5]:,d}")


# Purpose: Control the flow of the program.
# Name: main
# Parameters: None
# Return: None
def main():
    # Intro message
    print("**************************************************")
    print(" Welcome to the Movie Profit Analysis Program! ")
    print("**************************************************")
    print("\nThis program helps you analyze movie data from a CSV file.")
    print("\nLet's get started!\n")

    # Read the file into a table
    table = read_file()

    # Add the profit column
    table = profit_column(table)

    # Prompt the user for the output file name
    output_file = input("\nEnter the output CSV file name: ")

    # Write the updated table to the output file
    write_list_to_file(table, output_file)

    # Find and display the movie with the highest profit
    highest_profit_movie(table)

    # Exit message
    print("\n**************************************************")
    print(" Thank you for using the Movie Profit Analysis Program!")
    print("**************************************************")

main()