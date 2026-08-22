#1

def litres(time):
    return int(time * 0.5)

#2

def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

#3

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#4

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

#5

def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())