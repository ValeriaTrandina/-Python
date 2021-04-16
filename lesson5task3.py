# Задание 3

with open('new_file_3.txt') as f:
    salary = []
    poor = []
    list = f.read().split('\n')
    for i in list:
        i = i.split()
        if i in list < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Сотрудники с окладом меньше 20000 {poor}, Средний доход сотрудников {sum(map(int, salary)) / len(salary)}')