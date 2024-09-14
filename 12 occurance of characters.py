input_string = "Raja"
char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Count:")
for char, count in char_count.items():
    print(f"{char}: {count}")

 
