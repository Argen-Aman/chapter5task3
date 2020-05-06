class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def drive(self, km):
        l = km / 10
        if l <= self.fuel:
            self.__add_distance(km)
            self.__subtract_fuel(l)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, l):
        self.fuel -= l

my_car = Car('Honda', 'Civic', 2004)
print(my_car.drive(700))
print(my_car.drive(701))
