def factorial(n):
    try:        
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    except RecursionError:
        print("Recursion limit exceeded. Please enter a smaller number.")

# Example usage
number = int(input("Enter a number: "))
if number<0:
    print("Please enter a positive integer number.")
else:
    print(f"The factorial of {number} is {factorial(number)}")
