with open("numbers.txt", "r") as f:
    # Read the file into a list of numbers
    numbers = [int(line) for line in f if line.strip().isdigit()]
    # Find the maximum number
    max_number = max(numbers)
    print(max_number)

# Append the maximum number to the file
with open("numbers.txt", "w") as f:
    f.write (str(max_number))


