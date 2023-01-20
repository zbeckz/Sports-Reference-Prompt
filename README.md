# Sports-Reference-Prompt
For the Sports Reference 2023 Summer Internship Engineering Position

REQUIREMENTS:
1. Python (this was developed with version 3.11.1 and has NOT been tested in other versions)
2. Pandas library (instructions for installation found here: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

SOLUTION DESCRIPTION:
1. First read in the json file and convert into a python dictionary
2. Use this dictionary to find the number of teams, and create a 2D array with a row/column for each team
3. Loop through every row of the array. 
4. Within each row, first put a '--' in the diagonal of the array (where row = column) because teams do not play against themselves. 
5. Then, move loop from left to right within the row starting at column = row + 1. Retrieve the appropriate value from the dictionary (using the keys from the dictionary and the loop counters for row and column) and place into the current position of the matrix. Do this for the mirror position (switch row and column) as well. No need to loop through the lower left portion of the matrix because the data can be gathered from the same info needed to fill in the top right portion of the matrix
7. Finally, utilize a Pandas dataframe to neatly print a table containing the data in the completed matrix
