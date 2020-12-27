'''

'''
class Vehicle:
    def __init__(self,manufacturer,model,yearOfProduction):
        self.manufacturer=manufacturer
        self.model = model
        self.yearOfProduction = yearOfProduction
    def __repr__(self):
        return str(self.manufacturer) + " " + str(self.model) +  " ("+str(self.yearOfProduction)+")"
    def __eq__(self,other):
        if(self.manufacturer == other.manufacturer and self.model == other.model and self.yearOfProduction == other.yearOfProduction):
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,numberOfDoors,type):
        super().__init__(manufacturer,model,yearOfProduction)
        self.numberOfDoors=numberOfDoors
        self.type = type
    def __eq__(self,other):
        if(super(Car,self).__eq__(other) and self.type==other.type and self.numberOfDoors==other.numberOfDoors):
           return True
        else:
            return False 
    

class Truck(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,loadWeight):
        super().__init__(manufacturer,model,yearOfProduction)
        self.loadWeight = loadWeight

class Bus(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,numberOfSeats):
        super().__init__(manufacturer,model,yearOfProduction)
        self.numberOfSeats=numberOfSeats

class Part:
    def __init__(self,vehicle,name,number,price):
        self.vehicle = vehicle
        self.name=name
        self.number = number
        self.price = price
    def __repr__(self):
        return str(self.name) + " (" + str(self.vehicle) + ")-"+str(self.price)

auto = Car("Audi","A6",2016,5,"limo")

auto2 = Car("Audi","A",2016,5,"limo")



print(auto==auto2)