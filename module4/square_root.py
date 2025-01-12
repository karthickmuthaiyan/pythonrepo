import math

def calculate_q(d_values):
    C = 50
    H = 30
    result = []
    for D in d_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(int(Q))
    return result

# Input sequence
input_sequence = input("Enter comma-separated values: ")
d_values = [int(x) for x in input_sequence.split(",")]

# Calculate and print the result
output = calculate_q(d_values)
print("Output:",end="")
print(",".join(map(str,output)))