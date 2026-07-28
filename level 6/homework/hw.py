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