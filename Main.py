# Import the required modules
import math

# Variables
name = "John Doe"
age = 30
pi = math.pi

# Print a formatted string
print(f"My name is {name} and I am {age} years old. The value of pi is approximately {pi:.2f}")

# Lists
fruits = ['apple', 'banana', 'orange']

# Loops
print("\nFruits:")
for fruit in fruits:
    print(fruit)

# Conditionals
print("\nEven numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Functions
def square(x):
    return x * x

print("\nSquares:")
for i in range(1, 6):
    print(f"The square of {i} is {square(i)}")

# Classes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

print("\nCircle:")
circle = Circle(5)
print(f"A circle with radius 5 has an area of {circle.area():.2f} and a circumference of {circle.circumference():.2f}")

