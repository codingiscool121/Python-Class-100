class Cars(object):
    def __init__(self, price, model, color):
        self.name= model
        self.price = price
        self.color = color
    def getattributes(self):
        print(self.name, self.price, self.color)

toyota = Cars(10000,"Camry","Blue/Green")
honda = Cars(30000, "Pilot", "Bage")
print(toyota.getattributes(), honda.getattributes())


