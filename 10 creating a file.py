# Create a file with 10 lines of characters
with open("example.txt", "w") as file:
    for i in range(10):
        file.write(f"Line {i+1}: This is a sample text.\n")

# Ask the user to input the number of characters to read
n = int(input("Enter the number of characters to read from the start of the file: "))

# Read n characters from the start of the file
with open("example.txt", "r") as file:
    chars = file.read(n)

# Display the read characters in reverse order
print("Characters in reverse order:")
print(chars[::-1])