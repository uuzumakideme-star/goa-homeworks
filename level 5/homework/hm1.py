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