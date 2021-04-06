# Задание 4

my_string = input('Введите текст -')
my_string = my_string.split()
for i, el in enumerate(my_string, 0):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i} - {el}')














