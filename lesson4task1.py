# Задание 1

def salary():
    try:
        working_hours = float(input('Введите время работы в часах -'))
        rate = int(input('Введите ставку -'))
        premium = int(input('Введите сумму премии -'))
        result = working_hours * rate + premium
        print(f'Зарплата сотрудника {result}')
    except ValueError:
        return print('Введённое значение не является числом')
salary()