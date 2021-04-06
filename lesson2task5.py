# Задание 5

list = [4, 9, 3, 5, 1, 6]
num = int(input('Введите число -'))
a = list.count(num)
for el in list:
    if a > 0:
        i = list.index(num)
        list.insert(i+a, num)
        break
    else:
        if num > el:
            j = list.index(el)
            list.insert(j, num)
            break
        elif num < list[len(list) - 1]:
            list.append(num)
print(list)













