from itertools import count
my_list = [22, 11, 75, 22, 16, 2, 2, 2, 3, 4, 5, 3, 11, 234, 245, 56, 62]
new_list = [el for el in my_list if my_list.count(el) < 2]
