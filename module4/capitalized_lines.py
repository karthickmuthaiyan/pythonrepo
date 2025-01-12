def main():
    lines = []
    print("Enter lines of text (type 'END' to finish):")
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line.upper())
    
    print("\nCapitalized Lines:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()