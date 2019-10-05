import time


class Dog():
    def __init__ (self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def __repr__ (self):
        return f"{self.name} / age - {self.age} / {self.coat_color} coat."
    
    def coat(self):
        return f"{self.name}'s coat is {self.coat_color}."


class Car():
    def __init__ (self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __repr__ (self):
        return f"{self.color} car / mileage: {self.mileage}"
    
    def drive (self, miles):
        self.mileage += miles


philo = Dog('Philo', 5, 'brown')
print(philo.coat())
mustang = Car('blue', 20_000)
ferrari = Car('red', 30_000)
print(f'The {mustang.color} car has {mustang.mileage} miles')
print(f'The {ferrari.color} car has {ferrari.mileage} miles')
lamborghini = Car('yellow', 0)
print(lamborghini)
lamborghini.drive(100)
print(lamborghini)
time.sleep(8)
