def check_divisibility_by_5(binary_numbers):
    binary_list = binary_numbers.split(',')
    divisible_by_5 = []

    for binary in binary_list:
        decimal = int(binary,2)
        print(decimal)
        if decimal % 5 == 0:
            divisible_by_5.append(binary)

    return ','.join(divisible_by_5)

# Example usage
input_sequence = "1010,1111,1001,1100"
result = check_divisibility_by_5(input_sequence)
print(result)  # Output: 1010,1111