# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think

Tasks:
1. Read data from file to a table
2. Update the table by adding value/element at each to hold the profit
   3. For row in table:
      4. budget =
      5. demestic gross =
      6. worldwide gross =
      6. profit =
      7. row.append(profit)
3. Write the new table onto output file
4. Main function



Purpose: Read the data from the file into a table
Name: read_data
Parameters: file_name
Return: names
Algorithm:
1. Open the file specified by file_name for reading. 
2. Create an empty list names. 
3. For each line in the file:
   1. row = line.split 
   2. convert the number in strings to integers
   3. append row to table
4. Close the file. 
5. Return the table.

Purpose: Update the table by adding value/element at each to hold the profit
Name: 
Parameters: 
Return: 
Algorithm:
1. For row in table
   2. budget = row[2]
   3. Domestic Gross = row[3]
   4. Worldwide Gross = row[4]
   5. profit = Worldwide Gross - budget
   6. append profit to each row

Purpose: Write the new table onto output file
Name: 
Parameters: 
Return: 
Algorithm:
1. Create new file
2. If element is digit:
   3. Use string
   4. line = ''
   5. for item in row:
      6. if item isdigit()
         7. line = str(item + ',')
      7. line = item + ','

Purpose: Main
Name: Main() 
Parameters: 
Return: 
Algorithm: