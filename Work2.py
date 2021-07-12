my_list = [200, 400, 5, 10, 2, 2, 1, 3, 15, 72, 54, 61]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(f'Исходный список: {my_list}')
print(f'Результат: {new_list}')