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