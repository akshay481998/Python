class car:

    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def mileage(self):
        print("Mileage of this car")


c = car("solid","v6","Radial")
print(c)

class tata(car):
    pass

t = tata("solid1","v8","Radial1")
print(t)
print(t.mileage())