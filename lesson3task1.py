# Задание 1

#x = int(input('Введите первое число -'))
#y = int(input('Введите второе число -'))
# z = x / y
#

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не можеть быть равен нулю"
    except ValueError:
        return "Введите число"
print(my_func(int(input("Введите первое число = ")), int(input("Введите второе = "))))