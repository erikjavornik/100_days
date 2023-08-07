def add(*num):
    total = 0
    for n in num:
        total += n 
    return total

sum = add(1,2,3,4,5,6,7,8,9)
# print(sum)

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)
# calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make="Nissan", model="GTR")
print(my_car.model)