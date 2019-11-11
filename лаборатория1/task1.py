import re
print("Кулик Валерія Максимівна\n Лабораторна робота №1 \n Варіант 10 \n Завдання №1. Створення матриці ")
​
​
def int_input(text):
    while True:
        user_input = input(text)
        if re.match('^[-+]{0,1}[0-9]{1,}(\.[0-9]{1,}){0,1}$', user_input):
            break
        else:
            print("Помилка")
            continue
    return float(user_input)
​
​
k = int_input("Введіть число k : ")
a = int_input("Введіть число a : ")
b = int_input("Введіть число b : ")
c = int_input("Введіть число c : ")
​
​
if a % k != 0 and b % k != 0 and c % k != 0:
    print("k не є дільником жодного числа")
elif a % k == 0:
    print("число а")
elif b % k == 0:
    print("число б")
elif c % k == 0:
    print("число с")
