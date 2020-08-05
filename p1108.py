from math import *
import csv
class Store:
    name = "Provigo"
    address = (700,"Rue st Laurent", "Montreal", "QC", 22045, 52929)
    inventory = {
        "apple":(0.99, 7),
        "abanana":(1.99, 8),
        "orange":(2.99, 9),
        "watermelons":(6, 4)
        }
    def __init__(self, name = "provigo"):
        self.name = name
    
    def calculate_wealth(self):
        sum = 0
        for item in self.inventory.items():
            sum = sum + item[1][0] * item[1][1]
        return sum

    def outputDetails(self):
        return "{} is locataed at {} {} and has {} items ".format(
            self.name,
            self.address[0],
            self.address[1],
            self._getNumberOfItems()
            )

    def _getNumberOfItems(self):
        sum = 0
        for item in self.inventory.items():
            sum = sum + item[1][1]
        return sum
    def calculateDistance(self, x, y):
        y_diff = y - self.address[-1]
        y_sq = y_diff ** 2
        x_sq = (x - self.address[-2]) ** 2
        return sqrt(y_sq + x_sq)
    
    def addItemToInventory(self, itemName, quantity, price):
        if itemName in self.inventory.keys():
            currentTuple = self.inventory[itemName]
            listc = list(currentTuple)
            listc[1] = currentTuple[1] + quantity
            self.inventory[itemName] = tuple(currentInfo)
        else: self.inventory[itemName] = (quantity, price)
        return self.inventory
    
    def saveToCSV(self):
        with open("csv.csv", "w") as file:
            csvWriter = csv.writer(file)
            for i in self.inventory.items():
                csvWriter.writerow([i[0].strip(), i[1][0], i[1][1]])

    def _validateRow(self, row):
        if (len(row)==0 or row[0]==""):
            return False
        return True
        

    def readFromCSV(self):
        with open("csv.csv", "r") as file:
            reader = csv.reader(file)
            inventory = {}
            for row in reader:
                if (self._validateRow(row)):
                   inventory[row[0]] = (row[1], row[2])
            self.inventory = inventory

if __name__ == '__main__':
    store = Store()
    print(store.calculate_wealth())
    print(store.outputDetails())
    store.name = "Metro"
    print(store.calculateDistance(8 , 9))
##print(store.addItemToInventory("apple", 8 , 9))
    print("saving")
    print(store.saveToCSV())
    print("reading")
    print(store.readFromCSV())
else:
    print('fdalskdjf')
