name = "demetre"
for I in range(10):
    print(name)

for I in range(5, 31):
    print(I)

start = int(input("1"))
stop = int(input("31"))
for I in range(start, stop + 1):
    print(I)

n = int(input("5"))
name = input("demetre")
for I in range(n):
    print(name)

number = int(input("7"))

for i in range(1, 11):
    result = number ** i
    print(f"{number} ხარისხად {i} = {result}")

number = int(input("შემოიყვანეთ რიცხვი: "))

total_sum = 0

for i in range(1, number + 1):
    total_sum += i

print(f"1-დან {number}-ის ჩათვლით რიცხვების ჯამია: {total_sum}")