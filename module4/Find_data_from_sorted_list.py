def binary_search(sorted_list, target):
    index=-1
    for i in range(len(sorted_list)):
        if sorted_list[i] == target:
            index= i
    if index>=0:
        return index
    else:
        return -1

# Example usage
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(data, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")