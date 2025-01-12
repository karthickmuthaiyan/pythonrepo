# Program to sort a comma-separated sequence of words alphabetically

# Accept input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = input_sequence.split(',')

# Sort the list of words alphabetically
sorted_words = sorted(words)

# Join the sorted list back into a comma-separated string
sorted_sequence = ','.join(sorted_words)

# Print the sorted sequence
print("Sorted sequence:", sorted_sequence)