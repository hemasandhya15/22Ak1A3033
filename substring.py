def print_even_length_substrings(input_string):
    words = input_string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

input_string = "sun rises in the east"
print_even_length_substrings(input_string)
