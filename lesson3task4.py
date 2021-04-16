# Задание 4

x = int(input('Введите первое число -'))
y = int(input('Введите второое число -'))


def my_func(x, y):
    if x >= 0 and y < 0:
        return pow(x, y)
print(my_func(x, y))
