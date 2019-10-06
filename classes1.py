import time


class Dog():
    species = "Canis familiaris"
    
    def __init__ (self, name, age, coat_color): #instance initialization method
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def __repr__ (self): #instance representation with interpolation of the params
        return f"{self.name} / age - {self.age} / {self.coat_color} coat."

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def coat(self):
        return f"{self.name}'s coat is {self.coat_color}."


class GoldenRetriever(Dog): #inheritance of the class interface
    
    def speak(self, sound="Bark"):
        return super().speak(sound) #reference to the parent method


class Rectangle():

    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):

    def __init__ (self, side_length):
        self.length = side_length
        self.width = side_length


Mark = GoldenRetriever("Mark", 3, "blond") #GoldenRetriever instance initialization
print(Mark.speak())
a = Rectangle (3, 4) #Rectangle instance initialization
print(f'Area of a rectangle 3x4 is {a.area()}')
b = Square(4) #Square instace initialization
print(f'Area of a square 4x4 is {b.area()}') #reference to the parent method
time.sleep(5)
