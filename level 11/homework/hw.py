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