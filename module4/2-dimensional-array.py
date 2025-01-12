
X = int(input("Enter the number of rows: "))
"""
This script generates a 2-dimensional array based on user input for the number of rows and columns.
Each element in the array is the product of its row and column indices.
Steps:
1. Prompt the user to enter the number of rows (X).
2. Prompt the user to enter the number of columns (Y).
3. Create a 2-dimensional array where each element at position (i, j) is calculated as i * j.
4. Print the generated 2-dimensional array.
Example:
If the user inputs 3 for rows and 4 for columns, the output will be:
[[0, 0, 0, 0], 
 [0, 1, 2, 3], 
 [0, 2, 4, 6]]
"""
Y = int(input("Enter the number of columns: "))

array = [[i * j for j in range(Y)] for i in range(X)]

print(array)