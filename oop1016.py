from random import randint

class Vehicle:
    _color = 'green'
    tire_pressure = 300
    gas_meter = 5
    
class Car(Vehicle):
    _color = 'silver'
    age = 5
    tire_pressure = 20
    gas_meter = 80
    x_coordinate = 0
    def _init_(self, color,):
        self._color = color
        self.gas_meter = randint(0,100)

    def getter(self):
        return [self.tire_pressure, self.gas_meter]

    def setter(self, new_pressure, new_meter):
        self.tire_pressure = new_pressure
        self.gas_meter = new_meter

    def accelerate(self, distance, gas):
##        for i in range(int(distance)):
        while (self.gas_meter > 5 or self.x_coordinate > 200):
            if (self.gas_meter < 7):
               print('Need find a station and refuel immediatly!')
               break;
            elif(self.x_coordinate >199):
               print('Distance is enough')
               break;
            self.x_coordinate = self.x_coordinate + distance
            self.gas_meter = self.gas_meter - gas
        print("the total distance now is {}, the gas now remaining {}".\
              format(self.x_coordinate, self.gas_meter))
        return self.x_coordinate
    
    def acce(self, distance):
        for i in range(int(distance)):
            if self.gas_meter <=0:
                break
            self.gas_meter = self.gas_meter + 5
            self.x_coordinate = self.x_coordinate + 1
        print(self.x_coordinate)
        return self.x_coordinate
    
    def accel(self, distance):
        base_on_gas = self.gas_meter/5
        self.x_coordinate = self.x_coordinate + min(distance, base_on_gas)
        #min(5, 10)

    def refuel(self, volume):
        if (volume + self.gas_meter <= 100):
            self.gas_meter = self.gas_meter + volume
            print('the gas meter now is {}'.format(self.gas_meter))
        else:
            print('add {} fuel will be more than 100 over fill the tank'.\
                  format(volume))
    def addTirePressure(self, pressure):
        if (pressure <= 32):
            self.tire_pressure = pressure
            print('the tire pressure now is {}'.format(self.tire_pressure))
        else:
            print('add {} will be more than 32 pressure and damage the tire'.\
                  format(pressure))
    def totalDistance(self, distance):
        turn = 0
        total = 0
        while turn < 50:
            total = total + self.acce()
            turn = turn + 1

class BlueCar(Car):
    _color = 'blue'
    age = 1
    tire_pressure = 20
    gas_meter = 10
    x_coordinate = 0
    
class RedCar(Car):    
    _color = 'red'
    age = 2
    tire_pressure = 20
    gas_meter = 10
    x_coordinate = 0

