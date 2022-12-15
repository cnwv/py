class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'машина {self.name} стартует'
    def stop(self):
        return f'машина {self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью в {self.speed} км/ч')
        if self.speed > 60:
            return f'Превышение скорости на {self.speed - 60} км/ч'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью в {self.speed} км/ч')
        if self.speed > 40:
            return f'Превышение скорости на {self.speed - 40} км/ч'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'
audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(80, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.go())
print(lada.turn_left())
print(lada.show_speed())
print(oka.go())
print(oka.show_speed())
print(oka.turn_right())
print(audi.stop())
print(ford.go())