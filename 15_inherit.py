class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def speed_up(self):
        self.speed += 10

    def speed_dn(self):
        self.speed -= 10


class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        super().__init__(speed)
        self.wheels = wheels
        self.seats = seats

    def info(self):
        print(self.speed, self.wheels, self.seats)


car = Car(100, 4, 4)
car.speed_up()
car.info()


class Truck(Car):
    def __init__(self, speed, wheels, seats, loadage):
        super().__init__(speed, wheels, seats)
        self.loadage = loadage

    def load(self):
        print("load")

    def unload(self):
        print("unload")

    def info(self):
        print(self.speed, self.wheels, self.seats, self.loadage)


truck = Truck(100, 6, 2, 80)
truck.load()
truck.unload()
truck.speed_dn()
truck.info()
