#2

def add_numbers(a, b):
    return a + b

#3

def square(number):
    return number ** 2

#4

def is_even(number):
    return number % 2 == 0

#5

def greet(name):
    print(f"გამარჯობა, {name}!")

#6

def find_max(numbers):
    return max(numbers)

#7

def to_upper(text):
    return text.upper()

#8

def filter_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

#9

def filter_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

#10

def calculate_average(numbers):
    if not numbers:
        return "სია ცარიელია"
    return sum(numbers) / len(numbers)

#11

def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

