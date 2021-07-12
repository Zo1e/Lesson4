from itertools import count as cnt
from math import factorial as fact
def gen():
    for el in cnt(1):
        yield fact(el)

new_gen = gen()
i = 0
for x in new_gen:
    if i < 10:
        print(x)
        i += 1
    else:
        break
