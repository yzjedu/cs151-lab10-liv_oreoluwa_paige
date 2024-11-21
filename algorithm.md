# Algorithm Document

#### Write down the list of tasks to help you think

Tasks:
1. Read data from file to a table
2. Update the table by adding value/element at each to hold the profit
3. Write the new table onto output file
4. Find and display the movie with the highest profit.
5. Main function

 
* Purpose:  Read movie data from a CSV file and store it in a list of lists (table).
* Name: read_file
* Parameters: file_name 
* Return: table (list of lists)
* Algorithm:
1. Open the file specified by file_name for reading. 
2. Create an empty list called names_table. 
3. For each line in the file:
   1. Split the line by commas to create a list row 
   2. Convert the budget, domestic gross, and worldwide gross from strings to integers.
   3. Append row to table
4. Close the file. 
5. Return the table.

* Purpose: Update the table by adding a column to hold the profit
* Name: profit_column
* Parameters: table
* Return: The updated table with an additional profit column for each movie.
* Algorithm:
1. For each row in table:
   1. Extract the budget from row[2]
   2. Extract the worldwide_gross from row[4]
   3. Calculate the profit as worldwide_gross - budget.
   4. Append the profit value to the row.
2. Return the updated table

* Purpose: Write the updated table with the profit column to a new CSV file.
* Name: write_list_to_file
* Parameters: table, output file
* Return: None
* Algorithm:
1. Open the output file for writing.
2. For each row in the table:
   1. Initialize an empty string line
   2. For each value item in row:
      1. If item is an integer, convert it to a string
      2. Concatenate item (as a string) to line, followed by a comma.
   3. Remove the trailing comma from line.
   4. Write the line to the output_file, followed by a newline character.
3. Close the output_file.
4. Display a success message indicating that the file was written successfully.

* Purpose: Identify and display the movie with the highest profit from the table.
* Name: highest_profit_movie
* Parameters: table (list of lists)
* Return: None
Algorithm:
1. Initialize a variable max_profit_movie with the first row of the table. 
2. Initialize a variable max_profit with the profit value from the first row (row[-1]). 
3. For each row in the table:
   1. Extract the profit value from the last column (row[-1]). 
   2. If the profit is greater than max_profit:
      1. Update max_profit with the current row’s profit. 
      2. Update max_profit_movie with the current row.
4. Display the details of the movie with the highest profit

* Purpose: Control the flow of the program 
* Name: Main() 
* Parameters: None
* Return: None
* Algorithm:
1. Display a welcome message to the user. 
2. Prompt the user to enter the name of the input file (input_file). 
3. Call read_file(input_file) to read the movie data into a table. 
4. Call profit_column(table) to calculate and add the profit column to the table. 
5. Prompt the user to enter the name of the output file (output_file). 
6. Call write_data(table, output_file) to write the updated table to the output file. 
7. Call highest_profit_movie(table) to find and display the movie with the highest profit. 
8. Display a thank-you message to the user.