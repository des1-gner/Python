import math
import re
from collections import Counter

# Function 1: list_stats
def list_stats(numbers):
    total_sum = sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    average = total_sum / len(numbers)

    print("Sum:", total_sum)
    print("Max:", max_num)
    print("Min:", min_num)
    print("Mean:", average)

# Data and function call for list_stats
numbers = [10, 20, 30, 40, 50]
list_stats(numbers)
print()

# Function 2: has_common_member
def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Data and function call for has_common_member
list1 = ["dog", "cat", "lion", "tiger"]
list2 = ["lion", "elephant", "giraffe", "cat"]
print(has_common_member(list1, list2))
print()

# Function 3: combine_dictionaries
def combine_dictionaries(d1, d2):
    combined_dict = Counter(d1) + Counter(d2)
    return combined_dict

# Data and function call for combine_dictionaries
d1 = {'dog': 3, 'cat': 2, 'lion': 1}
d2 = {'lion': 2, 'cat': 1, 'tiger': 4}
combined_dict = combine_dictionaries(d1, d2)
print(combined_dict)
print()

# Function 4: fizz_buzz
def fizz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end="")
        elif num % 3 == 0:
            print("Fizz", end="")
        elif num % 5 == 0:
            print("Buzz", end="")
        else:
            print(num, end="")
    print()

# Function call for fizz_buzz
fizz_buzz()
print()

# Function 5: validate_password
def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

# Data and function call for validate_password
password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
print()

# Function 6: unique_list
def unique_list(input_list):
    return list(set(input_list))

# Data and function call for unique_list
sample_list = ["dog", "cat", "dog", "lion", "tiger", "tiger"]
unique = unique_list(sample_list)
print(unique)
print()

# Function 7: calculate_hypotenuse
def calculate_hypotenuse(height, base):
    hypotenuse = math.sqrt(height**2 + base**2)
    return hypotenuse

# Data and function call for calculate_hypotenuse
height = 5
base = 12
hypotenuse = calculate_hypotenuse(height, base)
print("Hypotenuse:", hypotenuse)
print()

# Function 8: calculate_scrabble_score
def calculate_scrabble_score(word):
    score = 0
    letter_values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    for letter in word.upper():
        score += letter_values.get(letter, 0)

    return score

# Data and function call for calculate_scrabble_score
word = "LION"
score = calculate_scrabble_score(word)
print("Scrabble score:", score)
print()

# Function 9: gcd
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Data and function call for gcd
num1 = 24
num2 = 36
result = gcd(num1, num2)
print("GCD:", result)
