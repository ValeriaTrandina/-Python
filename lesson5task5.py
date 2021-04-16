# Задание 5

def summary():
    try:
        with open('new_file_7.txt', 'w+') as file_obj:
            line = input('Введите набор чисел \n-')
            file_obj.writelines(line)
            number = line.split()
            print(sum(map(int, number)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Номер введён неверно')
summary()