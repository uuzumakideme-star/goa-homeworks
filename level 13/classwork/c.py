score = float(input("შეიყვანეთ თქვენი ქულა: "))

if score > 100 or score < 0:
    print("არასწორი ქულა")
elif score > 90 and score <= 100:
    print("საუკეთესო შედეგია!")
elif score > 70 and score <= 90:
    print("კარგი შედეგია!")
elif score > 50 and score <= 70:
    print("გადამსვლელი ქულა გადალახეთ!")
else:
    print("ვერ ჩააბარეთ")



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

last_four = numbers[4:]

print(last_four)


name = input("შეიყვანეთ თქვენი სახელი: ")

reversed_name = name[::1]

print(reversed_name)


