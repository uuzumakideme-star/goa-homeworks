# 1

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# 2

def add_binary(a, b):
    return bin(a + b)[2:]

# 3

def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)

# 4

def spin_words(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
            
    return " ".join(result)

