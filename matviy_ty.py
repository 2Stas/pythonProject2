import random
user = "1"
password = "2"
balance = 1000

hours = 0

new_password = password
def to_verify(user, password):
    user1 = input("Введіть логін: ")
    password1 = (input("Введіть пароль: "))
    if user1 == user and password1 == password:
        print("correct")
        global nigga
    else:
        print("incorrect user or password")

def to_change_pass(password):
    password1 = (input("Введіть пароль: "))
    user1 = input("Введіть логін: ")
    if user1 == user and password1 == password:
        password1 = (input("Введіть старий пароль: "))
        global new_password
        new_password = input("Введіть новий пароль: ")
        new_password = password
    else:
        return "get back to work nigga"
def to_take_money():
    take = input("Введіть сумму яку хочете зняти: ")
    global balance
    balance -= take
    print(f"Ваш баланс = {balance}")

def to_work(hours):
    hours = int(input("Введіть скільки годин працювати: "))
    global balance
    salary = hours * 40
    balance += salary

while True:
    anw = input("Введіть дію: ")
    if anw == "verify".lower():
        to_verify(user, password)
    elif anw == "change pass".lower().startswith("change"):
        to_change_pass(password)
    elif anw == "take money".lower().startswith("take"):
        to_take_money()
    elif anw == "work".lower():
        to_work(hours)



