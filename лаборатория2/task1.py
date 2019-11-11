import re
​
print("Кулик Валерія Максимівна\n "
      "Лабораторна робота №2 \n "
      "Варіант 10 \n "
      "Завдання №1. Обчислити формулу")
​
​
def int_input(text):
    while True:
        user_input = input(text)
        if re.match('^[0-9]{1,}$', user_input):
            break
        else:
            print("Помилка")
            continue
    return int(user_input)
​
​
def float_input(text):
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
n = int_input('Введіть n : ')
x = float_input('Введіть x : ')
​
res = 1
for i in range(1, n):
    res = res * ((x + i) / i*i)
​
print('Результат : ', res)
