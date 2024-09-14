def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test the function
s = "my name is raja"
print("Original string:", s)
print("Reversed words:", reverse_words(s))
