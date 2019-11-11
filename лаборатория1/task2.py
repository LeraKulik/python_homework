import re
​
print("Кулик Валерія Максимівна\n Лабораторна робота №1 \n Варіант 10 \n Завдання №3. Розв'язування рівнянь за певної умови(х): якщо х≥=8, то виконується рівність -х^2+х-9, якщо ж х<8, то виконується рівність -1/(x^4-6) ")
​
​
def data_input(text):
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
x = data_input('Введіть x : ')
​
​
lal = - x ** 2 + x - 9
lol = -1 / (x ** 4 - 6)
if x <= 8:
    print("- х ^ 2 + x - 9 = " + str(- x ** 2 + x - 9))
else:
    print("- 1 / (x ^ 4 - 6) = " + str(-1 / (x ** 4 - 6)))
