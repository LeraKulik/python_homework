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
n = int_input('Введіть n : ')
m = int_input('Введіть m : ')
​
for i in range(1, n):
    sum_e = 0
    for e in str(i):
        sum_e = sum_e + int(e)
    pow_sum_e = sum_e * sum_e
    if pow_sum_e == m:
        print(i)
