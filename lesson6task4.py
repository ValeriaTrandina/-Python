# Задание 4

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


ferrari = SportCar(147, 'Red', 'Ferrari', False)
volvo = TownCar(70, 'Gray', 'Volvo', False)
nissan = WorkCar(70, 'Green', 'Nissan', True)
mercedes = PoliceCar(110, 'Black',  'Mercedes', True)
print(nissan.turn_left())
print(f'When {volvo.turn_right()}, then {ferrari.stop()}')
print(f'{nissan.go()} with speed exactly {nissan.show_speed()}')
print(f'{nissan.name} is {nissan.color}')
print(f'Is {ferrari.name} a police car? {ferrari.is_police}')
print(f'Is {nissan.name}  a police car? {nissan.is_police}')
print(ferrari.show_speed())
print(volvo.show_speed())
print(mercedes.police())
print(mercedes.show_speed())