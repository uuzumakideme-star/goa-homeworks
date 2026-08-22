#1

age = int(input("შეიყვანეთ თქვენი ასაკი: "))
is_citizen = input("ხართ თუ არა მოქალაქე? (yes/no): ").strip().lower()

if age >= 18 and is_citizen == "yes":
    print("შესვლა ნებადართულია")
else:
    print("შესვლა აკრძალულია")

#2

numbers = [4, 12, 7, 25, 3, 18, 10, 30]

for num in numbers:
    if num > 10:
        print(num)

#3

cities = ["თბილისი", "ბათუმი", "ქუთაისი", "თელავი", "რუსთავი", "ზუგდიდი"]
index = int(input("შეიყვანეთ ინდექსი (0-დან 5-ის ჩათვლით): "))

print(cities[index])

#4

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > 100 or num2 > 100:
    print("პირობა შესრულდა")
else:
    print("პირობა არ შესრულდა")

#5

numbers = [12, 5, 8, 21, 34, 7, 9, 50, 16, 3]

for num in numbers:
    if num % 2 == 0:
        print(num)

#6

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ფორთოხალი", "მარწყვი", "ალუბალი", "კივი", "ანანასი", "ნესვი"]
first_five = fruits[:5]

print(first_five)

#7

numbers = [50, 120, 85, 300, 42, 105, 99, 210, 15, 500]
i = 0

while i < len(numbers):
    if numbers[i] > 100:
        print(numbers[i])
    i += 1

#8

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
every_second = items[::2]

print(every_second)

#9

numbers = [10, -5, 60, 25, 0, 100, 45, -12, 80, 30]

for num in numbers:
    if num > 50 or num < 0:
        print("დიდია")
    else:
        print("ნორმალური")

#10

temp = float(input("შეიყვანეთ ტემპერატურა: "))

if temp < 0 or temp > 35:
    print("ექსტრემალური ტემპერატურაა")
else:
    print("ტემპერატურა ნორმალურია")
