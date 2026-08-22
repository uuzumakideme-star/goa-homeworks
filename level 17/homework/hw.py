#1

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

#2

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

#3

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

#4

def litres(time):
    return int(time * 0.5)

#5

def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)