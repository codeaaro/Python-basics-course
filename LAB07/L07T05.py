class car:
    brand = ""
    model = ""
    price = 0

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

car1 = car("BMW", "750Li", 150000)
car2 = car("Volkswagen", "Polo", 15000)
car3 = car("Tesla", "CyberTruck", 80000)

hinta = car1.price+car2.price+car3.price

print("auto:",car1)
print("auto:",car2)
print("auto:",car3)
print("Autojen hinta yhteensä:",hinta)
