def add(*args):
	print(args[0])
	sum = 0
	for n in args:
		sum += n
	return sum

print(add(1, 5, 5, 7, 10, 20))


def calculate(n, **kwargs):
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(2, add=3, multiply=5)
25

# class Car:
#
# 	def __init__(self, **kw):
# 		self.make = kw["make"]
# 		self.model = kw["model"]
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)
# GT-R

#If we try to initialize the object without the model, we get a KeyError.

class Car:

	def __init__(self, **kw):
		self.make = kw.get("make")
		self.model = kw.get("model")
		self.colour = kw.get("colour")
		self.seats = kw.get("seats")

# my_car = Car(make="Nissan")
# print(my_car.model)
# None
my_car = Car(make="Audi", model="A6")
print(my_car.model)