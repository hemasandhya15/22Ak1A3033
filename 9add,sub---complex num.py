class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Test the class
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(2, 1)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Conjugate of num1:", num1.conjugate())
print("Conjugate of num2:", num2.conjugate())
