







# Purpose:
# Parameters: filename
# Return: table
def read_file(filename):
    table = []
    try:
        file = open(filename, 'r')
        for line in file:
            row = line.split
            table.append(row)
    except FileNotFoundError:
        print("File not found")
    return table

# Purpose:
# Parameters:
# Return:
def add_profit():
    for row in table:
        budget = row[2]
        domestic_gross = row[3]
        world_gross = row[4]
        profit = (domestic_gross + world_gross) - budget
        row.append(profit)

# Purpose:
# Parameters:
# Return:
def print_table(table):


