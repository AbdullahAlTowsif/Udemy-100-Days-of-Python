# kwargs: Many Keyworded Arguments (Keyword Arguments)
# It's type is Dictionary

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")

"""If I don't give any arguments in this case it will give us error.
To modify the error we have to use get function. """

# my_car = Car(make = "Nissan", model= "GT-R")

# Now if I miss any arg. it will show use none
my_car = Car(make = "Nissan")

# print(my_car.make)
print(my_car.model)

