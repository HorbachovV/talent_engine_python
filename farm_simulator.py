# Farm Simulator

# The task is to finish the code and get classes that define farm. The Farm is the class for a farm, each object should have attributes that define:

# name (str - the name of the farm object)
# square (floor - in ha)
# sheep (int - count of sheep in a farm)
# cows (int - count of cows in a farm)
# chickens (int - count of chickens in a farm)
# Class Farm itself contain class attributes that define prices for 1 unit of each entity such as cow, sheep and chicken and for 1 ha of the square:

# price_sheep
# price_cow
# price_chicken
# price_square
# The task is to fill the realization for a few methods:

# Finish __init__ method that should assign attributes name, square, sheep, cows, chickens to the instance.
# The class should have a method called get_value which should return the total money value of the farm.
# The class also should have the method __eq__(self, other) (to compare two farms) and __gt__(self, other) (> greater than). These are standard "magic" methods - they both receive two args - self and other where other is the object you are comparing self with.
# The tests for this will create two farms using Farm class you should finish creating and compare those instances with == and >.

class Farm:
    price_sheep = 500
    price_cow = 1000
    price_chicken = 50
    price_square = 700
    
    def __str__(self):
        return f'Farm "{self.name}", sq: {self.square} ha, value: ${self.get_value()}'

    def __init__(self, name, square, sheep, cows, chickens):
        self.name = name
        self.square = square
        self.sheep = sheep
        self.cows = cows
        self.chickens = chickens
    
    def get_value(self):
        value = self.sheep * Farm.price_sheep + self.cows * Farm.price_cow + self.chickens * Farm.price_chicken + self.square * Farm.price_square
        return value
    
    def __eq__(self, other):
        return self.get_value() == other.get_value()
        
    def __gt__(self, other):
        return self.get_value() > other.get_value()

# Simple Test
farm1 = Farm("My First Farm", 400, 10, 10, 10)
farm2 = Farm("My Second Farm", 300, 40, 30, 20)

print(farm1)
print(farm2)
print(farm1 > farm2)