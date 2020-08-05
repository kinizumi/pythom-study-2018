from random import randint
import csv

class Car:
    """
    some docummens
    and this is also the doc
    .....
    """
    color = 'red'
    gas_mileage = 0.1
    gas_level = 50
    position = 0

    def __init__(self, color):
        self.color = "blue"
    
    def move(self, distance):
        'Move a distance'
        d = self.gas_level / self.gas_mileage
        actual = min (d, distance)
        self.position = self.position + distance
        self.gas_level = self.gas_level - distance * distance

    

    def saveToCSV(self):
         with open("csv.csv", "w") as file:
             csvWriter = csv.writer(file)
             csvWriter.writerow(["total position", self.position])
    
    def readCSV(self):
        with open("csv.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                    print(row)
                    
class ElectricCar(Car):
    price = 20000
    tire_circle = 99

    def __init__(self):
        Car.__init__(self, "blue")
        
    def reprice(self, new_price):
        self.price = new_price

    def move(self, distance):
        self.changeTire(distance)
        self.position = self.position + distance
        
    def changeTire(self, distance):
        f = ( self.position + distance ) // self.tire_circle
        for i in f:
            print("change tire at {} time and go in this journey ".format(i))
        
myCar = ElectricCar()
myCar.reprice(15647)
print(myCar.price)
myCar.move(randint(1, 9999))
print(myCar.position)    
myCar.move(randint(1, 9999))
print(myCar.position)
myCar.move(randint(1, 9999))
print(myCar.position)

            
##class Employee:
##    def doWork(self):
##        print("working...")
##
##
##    
##class newE(Employee):
##    pass
##class manager(Employee):
##    def doWork(self):
##        print("chat on phone")

##car.move(500)
##print(car.position)
##car.move(600)
##print(car.position)
##car.move(50)
##print(car.position)
##car.saveToCSV()
##car.readCSV()
##print(car.move(23).__doc__)
                
