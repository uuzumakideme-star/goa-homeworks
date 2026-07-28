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