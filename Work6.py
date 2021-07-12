from itertools import count
for el in count(int(input('Введите начальное число - '))):
    print(el)
    if el == 60:
        break