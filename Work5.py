from functools import reduce
def func(prev_el, el):
    return prev_el * el
my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(reduce(func, my_list))
