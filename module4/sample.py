"""        
def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if (__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print("fact is",fact(int(sys.argv[1])))
"""
numbers = [1, 2, 3, 4]
strings = print(','.join(map(str, numbers)))

# Convert the map object to a list
#result = list(strings) 
print(strings)