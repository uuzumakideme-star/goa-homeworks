#1

def sum_to_n(n):
    return sum(range(n + 1))

#2

def count_positives(numbers):
    return sum(1 for num in numbers if num > 0)

#3

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

#4

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#5

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return "სიაში არ არის საკმარისი განსხვავებული რიცხვები"
    unique_numbers.sort()
    return unique_numbers[-2]

