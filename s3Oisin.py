# 1

def list_stats(numbers):
    total_sum = sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    average = total_sum / len(numbers)
    
    print("Sum:", total_sum)
    print("Max:", max_num)
    print("Min:", min_num)
    print("Mean:", average)

numbers = [1, 2, 3, 4, 5]
list_stats(numbers)

# 2

def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = ["Tom", "Bob", "Sue", "Rachel"]
list2 = ["Bob", "Susan", "Roger", "Mike"]
print(has_common_member(list1, list2))

from collections import Counter

# 3

def combine_dictionaries(d1, d2):
    combined_dict = Counter(d1) + Counter(d2)
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = combine_dictionaries(d1, d2)
print(combined_dict)

# 4

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

fizz_buzz()

# 5

import re

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

password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")

#6

def unique_list(input_list):
    return list(set(input_list))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique = unique_list(sample_list)
print(unique)

#7

import math

def calculate_hypotenuse(height, base):
    hypotenuse = math.sqrt(height**2 + base**2)
    return hypotenuse

height = 3
base = 4
hypotenuse = calculate_hypotenuse(height, base)
print("Hypotenuse:", hypotenuse)

#8

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

word = "Cabbage"
score = calculate_scrabble_score(word)
print("Scrabble score:", score)

#9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 12
num2 = 18
result = gcd(num1, num2)
print("GCD:", result)

