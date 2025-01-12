def remove_duplicates_and_sort(input_string):
    words = input_string.split()
    unique_words = sorted(set(words))
    return ' '.join(unique_words)

if __name__ == "__main__":
    input_string = input("Enter a sequence of whitespace separated words: ")
    result = remove_duplicates_and_sort(input_string)
    print(result)