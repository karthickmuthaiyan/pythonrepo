import math

# Example list of floating point numbers
numbers = [0.1, 0.2, 0.3, 0.4, 0.5]

# Using the built-in sum function
sum_result = sum(numbers)
print("Sum using built-in sum function:", sum_result)

# Using the math.fsum function
fsum_result = math.fsum(numbers)
print("Sum using math.fsum function:", fsum_result)