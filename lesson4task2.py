# Задание 2

first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in first_list if el > first_list[first_list.index(el)-1]]
print(new_list)