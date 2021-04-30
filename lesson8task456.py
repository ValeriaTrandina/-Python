# Задание 4, 5, 6

class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за штуку': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за штуку '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за штуку': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка'

        print(f'Чтобы завершить - нажмите F, чтобы продолжить продолжение - нажмите Enter')
        f = input(f'---> ')
        if f == 'F' or f == 'f':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.reception(self)


class Phone(OfficeEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Printer(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Phone('Panasonic', 1340, 9, 18)
unit_2 = Printer('Brother', 2680, 3, 9)
unit_3 = Scanner('Brother', 900, 2, 8)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

