from itertools import cycle
my_list = [22.4, 'Hello', 32, False]
i = 0
for el in cycle(my_list):
    if i > 25:
        break
    print(el)
    i += 1
