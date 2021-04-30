# Задание 2

class DivisionError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Ошибка")


div = DivisionError(87, 0)
print(DivisionError.divide_by_null(10, 0))
print(div.divide_by_null(100, 0))