# Задание 5

def my_sum ():
    sum_res = 0
    a = False
    while a == False:
        num = input('Введите несколько чисел - ').split()

        res = 0
        for el in range(len(num)):
            if num[el] == 'k' or num[el] == 'K':
                a = True
                break
            else:
                res = res + int(num[el])
        sum_res = sum_res + res
        print(f'Сумма чисел {sum_res}')
    print(f'Итоговая сумма {sum_res}')

my_sum()
