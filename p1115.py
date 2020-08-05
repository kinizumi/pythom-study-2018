##class Product:
##    """
##    doc_doc_doc
##    """
##    name = ''
##    price = 0
##
##    def __init__(self, name, price):
##        self.name = name
##        self.price = price
##        
##    def __lt__(self, other):
##        return self.price < other.price
##
##    def __le__(self, other):
##        return self.price <= other.price
##    
##    def __gt__(self, other):
##        return self.price > other.price
##
##    def __ge__(self, other):
##        return self.price >= other.price
##    
##    def __eq__(self, other):
##        return self.price == other.price
##    
##    def __ne__(self, other):
##        return self.price != other.price
##    
##    def __repr__(self, other):
##        return self.price != other.price
##
##    def __str__(self):
##        return "price is %s name is %s "%(self.price, self.name)
##
##    def __repr__(self):
##        return "name is %s !!!"%self.name
##
##    def __add__(self, tax):
##        return self.price + tax
##    
##    def __sub__(self, disc):
##        return self.price - disc
    

class Line:
    name = "vertical_line"
    length = 200
    number_of_stations = 0
    stations = []
    arrive_time = 0
    
    
    def __init__(self, name, stations):
        self.name = name
        self.stations = stations

    def find_transfer(self):
        for s in self.stations:
            if s.transfer_station:
                return s
        
    def same_line_stations(self, station1, station2, car):
        if station1 in self.stations and station2 in self.stations:
            return self.calc_time(station1, station2, car)
        elif station1 in self.stations:
            return self.calc_time(station1, self.find_transfer(), car)
        elif station2 in self.stations:
            return self.calc_time(station2, self.find_transfer(), car)
        else:
            return "something went wrong"
        
    def calc_time(self, station1, station2, car):
        return (station1.position - station2.position)/car.speed
            
        

class Station:
    name = ""
    uid = 0
    position = 0
    start_station = False
    end_station = False
    transfer_station = False
    
    def __init__(self, name, point, transfer)
    
class Car:
    uid = 0
    speed = 10
    


