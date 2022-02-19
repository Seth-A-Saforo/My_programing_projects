class Cars:
    def __init__(self, brand, doors, fuel_type):
        self.brand = brand
        self.doors = doors
        self.fuel_type = fuel_type

    def intro(self):
        print('My ' + self.brand + ' is reversing, please beware')


car1 = Cars('Corolla', 4, 'diesel')

car1.brand = 'Range rover'

#del car1.fuel_type
print(car1.fuel_type)
car1.intro()

