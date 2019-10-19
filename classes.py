import time


class Dog():
    def __init__ (self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def __repr__ (self):  # representation of an instance with interpolated params
        return f"{self.name} / age - {self.age} / {self.coat_color} coat."
    
    def coat(self):
        return f"{self.name}'s coat is {self.coat_color}."


class Car():
    def __init__ (self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __repr__ (self):  # representation of an instance with interpolated params
        return f"{self.color} car / mileage: {self.mileage}"
    
    def drive (self, miles):
        self.mileage += miles


philo = Dog('Philo', 5, 'brown')  # instance of the Dog class
print(philo.coat())  # call the instance method
mustang = Car('blue', 20_000)  # instance of the Car class
ferrari = Car('red', 30_000)  # instance of the Car class
print(f'The {mustang.color} car has {mustang.mileage} miles')  # interpolation of the instance params
print(f'The {ferrari.color} car has {ferrari.mileage} miles')  # interpolation of the instance params
lamborghini = Car('yellow', 0)  # instance of the Car class
print(lamborghini)  # check instance state with __repr__ method
lamborghini.drive(100)  # call the class method to change instance's params
print(lamborghini)  # check instance state with __repr__ method
time.sleep(8)
