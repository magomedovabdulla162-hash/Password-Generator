import secrets
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase = "abcdefghijklmnopqrstuvwxyz"

digits = "0123456789"

special = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

if use_uppercase:
    characters += uppercase

if use_lowercase:
    characters += lowercase

if use_digits:
    characters += digits

if use_special:
    characters += special

password = ""
for i in range(12):
    password += secrets.choice(characters)
print(password)

def get_password_length():
    length = int(input("Введите длину пароля: "))
    if length <= 0:
        print("Длина пароля должна быть больше нуля.")
