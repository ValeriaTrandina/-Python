# Задание 3
a = int(input('Введите первое число -'))
b = int(input('Введите второое число -'))
c = int(input('Введите третьее число -'))

def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c

print(my_func(a, b, c))