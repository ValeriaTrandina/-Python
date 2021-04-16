# Задание 2

p = ['Дерево\n', 'Куст\n', 'Цветок\n', 'Травинка\n']
with open('new_file_2.txt', 'w+') as f:
    f.writelines(p)
with open('new_file_2.txt') as f:
    lines = 0
    letters = 0
    for line in f:
        lines = lines + line.count('\n')
        letters = len(line) - 1
        print(f'{letters} букв_ы в строке')
    print(f'Количество строк {lines}')
    











