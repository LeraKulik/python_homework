import re
​
print("Кулик Валерія Максимівна\n "
      "Лабораторна робота №2 \n "
      "Варіант 10 \n "
      "Завдання №1. Обчислити формулу")
​
​
def int_input(text_mes):
    """
    Повертає ціле число
    :param text_mes: str, text, 'Введіть n : '
    :return: int, number, 1
    """
    while True:
        user_input = input(text_mes)
        if re.match('^[0-9]{1,}$', user_input):
            break
        else:
            print("Помилка")
            continue
    return int(user_input)
​
​
def main(s, n):
    """
    Головний алгоритм
    :param s: str, 'word1 word2', 'qwe wqe qwe'
    :param n: int, number, 1
    :return: None
    """
    text = s.split(' ')
    result = []
    for word in text:
        if n < len(word):
            result.append(word[0].upper() + word[1:])
        else:
            result.append(word)
    print(' '.join(result))
​
​
stroke = input("Введіть текст : ")
num = int_input("Введіть n :")
​
main(stroke, num)
