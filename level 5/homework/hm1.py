# level 1

name = "demetre"
lastname = "lezhava"
color = "purple"
print(name)
print(lastname)
print(color)

name = "demetre"
lastname = "lezhava"
age = 15
color = "purple"
city = "Batumi"

# level 2

#sololearn getting started with python

# level 3

#sololearn going deeper with python

name = "demetre"
surname = "lezhava"
age = 15
city = "batumi"
favorite_color = "purple"

print(name)
print(surname)
print(age)
print(city)
print(favorite_color)

first_name = "Saba"
age = 16
country = "Tbilisi"

print(first_name)
print(age)
print(country)

feri = "Black"
saxeli = "Saba"
asaki = 16

print(feri)
print(saxeli)
print(asaki)

# level 4

# input() ფუნქცია გამოიყენება მომხმარებლისგან ტერმინალის მეშვეობით მონაცემების მისაღებად.
# როდესაც პროგრამა მიაღწევს input()-ს, ის პაუზდება და ელოდება, სანამ მომხმარებელი
# ტექსტს აკრეფს და Enter კლავიშს დააჭერს.
# მნიშვნელოვანია: input() ფუნქციის მიერ დაბრუნებული ნებისმიერი მონაცემი 
# ყოველთვის არის ტექსტურ (string) ფორმატში!

# str (String - ტექსტური ტიპი):
# გამოიყენება ტექსტური ინფორმაციის შესანახად. იწერება ბრჭყალებში (" " ან ' ').
name = "საბა" 

# int (Integer - მთელი რიცხვი):
# გამოიყენება მთელი დადებითი ან უარყოფითი რიცხვების შესანახად (ათწილადების გარეშე).
age = 16 

# float (Floating-point number - ათწილადი რიცხვი):
# გამოიყენება წილადი/ათწილადი რიცხვების შესანახად, სადაც წერტილი გამოყოფს მთელ ნაწილს.
height = 1.75 

# bool (Boolean - ლოგიკური ტიპი):
# შეიცავს მხოლოდ ორ მნიშვნელობას: True (ჭეშმარიტი) ან False (მცდარი). 
# გამოიყენება პირობების შემოწმებისას.
is_student = True

first_name = input("შეიყვანეთ თქვენი სახელი: ")
last_name = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
city = input("შეიყვანეთ თქვენი ქალაქი: ")
favorite_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")

print("\n--- შეყვანილი ინფორმაცია ---")
print("სახელი:", first_name)
print("გვარი:", last_name)
print("ასაკი:", age)
print("ქალაქი:", city)
print("საყვარელი ფერი:", favorite_color)

user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")

print(user_name)
print(user_age)

# level 5

name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

print(f"გამარჯობა, მე ვარ {name}, ჩემი გვარია {surname} და ვარ {age} წლის.")

num1 = float(input("შეიყვანეთ პირველი ათწილადი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე ათწილადი რიცხვი: "))

print("ჯამი:", num1 + num2)
print("სხვაობა:", num1 - num2)
print("ნამრავლი:", num1 * num2)
print("განაყოფი:", num1 / num2)

var_str = "Python"
var_int = 25
var_float = 3.14
var_bool = True
var_input = input("შეიყვანეთ ნებისმიერი ტექსტი: ")

print(type(var_str))
print(type(var_int))
print(type(var_float))
print(type(var_bool))
print(type(var_input))

name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
fav_number = float(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))

print("სახელი:", name, "ტიპი:", type(name))
print("ასაკი:", age, "ტიპი:", type(age))
print("საყვარელი რიცხვი:", fav_number, "ტიპი:", type(fav_number))

word = input("შეიყვანეთ სიტყვა: ")
number = int(input("შეიყვანეთ რიცხვი: "))

print(f"შენ შეიყვანე სიტყვა: {word} და რიცხვი: {number}")

# level 6

name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
height = float(input("შეიყვანეთ თქვენი სიმაღლე (სმ-ში): "))

print(f"სახელი: {name}, ასაკი: {age}, სიმაღლე: {height}სმ")

is_adult_and_tall = age >= 18 and height > 170
print("არის სრულწლოვანი და 170 სმ-ზე მაღალი?:", is_adult_and_tall)

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

has_positive = num1 > 0 or num2 > 0
print("არის ერთ-ერთი მაინც დადებითი?:", has_positive)

my_favorite_color = "blue"  # ჩემი საყვარელი ფერი

user_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")
user_age = int(input("შეიყვანეთ თქვენი ასაკი: "))

result = (user_color.lower() == my_favorite_color) or (user_age < 18)
print(result)

name = input("შეიყვანეთ თქვენი სახელი: ")
balance = float(input("შეიყვანეთ ანგარიშზე არსებული თანხა: "))

vip_input = input("გაქვთ VIP სტატუსი? (yes/no): ")
is_vip = vip_input.lower() == "yes"

can_access = balance > 100 or is_vip
print(can_access)

# level 7

for i in range(100, 201):
    print(i)

name = "demetre"  # ჩაწერეთ თქვენი სახელი

for i in range(100):
    print(name)

first_name = input("შეიყვანეთ თქვენი სახელი: ")
last_name = input("შეიყვანეთ თქვენი გვარი: ")

full_name = first_name + " " + last_name

for i in range(50):
    print(full_name)

name = input("შეიყვანეთ თქვენი სახელი: ")
number = int(input("შეიყვანეთ რიცხვი: "))

for i in range(1, number):
    print(f"{name} = {i}")

number = int(input("შეიყვანეთ რიცხვი: "))

product = 1  

for i in range(1, number + 1):
    product *= i  

print("ნამრავლი 1-იდან შემოყვანილ რიცხვამდე არის:", product)

# level 8

n = int(input("შეიყვანეთ რიცხვი: "))

for i in range(1, n + 1):
    print(i)

start = int(input("შეიყვანეთ start: "))
stop = int(input("შეიყვანეთ stop: "))
step = int(input("შეიყვანეთ step: "))

for i in range(start, stop, step):
    print(i)

first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

for i in range(50):
    print(first_name, last_name)

n = int(input("შეიყვანეთ რიცხვი n: "))

for i in range(n, -1, -1):
    print(i)

n = int(input("შეიყვანეთ რიცხვი n: "))
i = 0

while i <= n:
    squared = i ** 2
    is_even = squared % 2 == 0
    print(f"რიცხვი: {i}, კვადრატი: {squared} -> {is_even}")
    i += 1

n = int(input("შეიყვანეთ რიცხვი: "))
i = 10

while i <= n:
    print(i)
    i += 1

start = int(input("შეიყვანეთ start: "))
stop = int(input("შეიყვანეთ stop: "))

i = start
while i <= stop:
    print(i)
    i += 1

name = input("შეიყვანეთ თქვენი სახელი: ")
count = 0

while count < 50:
    print(name)
    count += 1

total_sum = 0

while True:
    num = int(input("შეიყვანეთ რიცხვი (უარყოფითი დასრულებისთვის): "))
    if num < 0:
        break
    total_sum += num

print("შეყვანილი დადებითი რიცხვების ჯამი:", total_sum)

secret_number = 73
guess = None

while guess != secret_number:
    guess = int(input("გამოიყანით საიდუმლო რიცხვი: "))
    if guess != secret_number:
        print("არ არის სწორი, სცადეთ თავიდან!")

print("გილოცავთ! თქვენ გამოიცანით საიდუმლო რიცხვი!")

# level 9

score = int(input("შეიყვანეთ გამოცდის ქულა (0-100): "))

if score < 0 or score > 100:
    print("არასწორი ქულა")
elif score >= 91:
    print("A")
elif score >= 81:
    print("B")
elif score >= 71:
    print("C")
elif score >= 61:
    print("D")
else:
    print("F")

positive_count = 0
negative_count = 0
even_count = 0
odd_count = 0

print("გთხოვთ შეიყვანოთ 10 რიცხვი:")

for i in range(10):
    num = int(input(f"შეიყვანეთ რიცხვი #{i + 1}: "))
    
    # დადებითი / უარყოფითი (0 არც დადებითია და არც უარყოფითი)
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
        
    # ლუწი / კენტი
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n--- შედეგები ---")
print("დადებითი რიცხვების რაოდენობა:", positive_count)
print("უარყოფითი რიცხვების რაოდენობა:", negative_count)
print("ლუწი რიცხვების რაოდენობა:", even_count)
print("კენტი რიცხვების რაოდენობა:", odd_count)

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print("პირველი რიცხვი მეტია")
elif num2 > num1:
    print("მეორე რიცხვი მეტია")
else:
    print("რიცხვები ტოლია")

correct_password = "python123"  # სწორი პაროლი
attempts_left = 3  # სიცოცხლეების (ცდების) რაოდენობა

while attempts_left > 0:
    password_input = input("შეიყვანეთ პაროლი: ")
    
    if password_input == correct_password:
        print("წვდომა ნებადართულია! კეთილი იყოს თქვენი მობრძანება.")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"არასწორი პაროლია! დარჩენილი ცდები: {attempts_left}\n")
        else:
            print("ცდების რაოდენობა ამოეწურა. წვდომა უარყოფილია!")

# level 10 sololearn working with lists

# level 11

age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age >= 18:
    print("სრულწლოვანი ხართ")
else:
    print("არასრულწლოვანი ხართ")

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > 0 and num2 > 0:
    print("ორივე რიცხვი დადებითია")
else:
    print("ერთ-ერთი მაინც არ არის დადებითი")

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print("ერთ-ერთი მაინც ლუწია")
else:
    print("ორივე კენტია")

num_str = input("შეიყვანეთ რიცხვი: ")
num_int = int(num_str)

print("რიცხვის კვადრატია:", num_int ** 2)

score = int(input("შეიყვანეთ ქულა (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

for i in range(1, 21):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ფორთოხალი", "ალუბალი"]

print("პირველი ელემენტი:", fruits[0])
print("ბოლო ელემენტი:", fruits[-1])
print("მესამე ელემენტი:", fruits[2])

numbers = [10, 25, 30, 47, 52]

for num in numbers:
    print(num)

user_numbers = []

for i in range(5):
    num = int(input(f"შეიყვანეთ რიცხვი #{i + 1}: "))
    user_numbers.append(num)

print("შექმნილი სია:", user_numbers)

items = ["ა", "ბ", "გ", "დ", "ე", "ვ", "ზ", "თ"]

for index in range(0, len(items), 2):
    print(f"ინდექსი {index}: {items[index]}")

n = int(input("შეიყვანეთ რიცხვი N: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"1-დან {n}-მდე რიცხვების ჯამია:", total_sum)

n = int(input("შეიყვანეთ რიცხვი: "))
i = 1

while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

numbers_list = [12, 7, 5, 20, 33, 44, 91, 100]
even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("ლუწი რიცხვების რაოდენობა:", even_count)
print("კენტი რიცხვების რაოდენობა:", odd_count)

a = float(input("შეიყვანეთ პირველი რიცხვი: "))
b = float(input("შეიყვანეთ მეორე რიცხვი: "))
c = float(input("შეიყვანეთ მესამე რიცხვი: "))

if a == b == c:
    print("ყველა რიცხვი ტოლია")
elif a == b or a == c or b == c:
    print("ორი რიცხვი ტოლია")
else:
    print("ყველა რიცხვი განსხვავებულია")

