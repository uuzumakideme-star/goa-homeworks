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