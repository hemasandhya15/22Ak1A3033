# Read a 40-digit integer
num1 = int(input("Enter a 40-digit integer: "))

# Create two more 40-digit integers
num2 = num1 + 1
num3 = num1 - 1

# Demonstrate relational operations
print("Relational Operations:")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")

print(f"{num1} == {num3}: {num1 == num3}")
print(f"{num1} != {num3}: {num1 != num3}")
print(f"{num1} < {num3}: {num1 < num3}")
print(f"{num1} <= {num3}: {num1 <= num3}")
print(f"{num1} > {num3}: {num1 > num3}")
print(f"{num1} >= {num3}: {num1 >= num3}")