#2

name = input("შეიყვანეთ სახელი: ")
formatted_name = name.capitalize()
print(formatted_name)

#3

text = input("შეიყვანეთ ტექსტი: ")
upper_text = text.upper()
print(upper_text)

#4

text = input("შეიყვანეთ ტექსტი: ")
lower_text = text.lower()
print(lower_text)

#5

sentence = input("შეიყვანეთ წინადადება: ")
search_word = input("შეიყვანეთ საძიებელი სიტყვა: ")

position = sentence.find(search_word)

if position != -1:
    print(f"სიტყვა იწყება პოზიციაზე: {position}")
else:
    print("სიტყვა წინადადებაში ვერ მოიძებნა.")
