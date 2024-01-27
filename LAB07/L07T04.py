class mobile:
    brand = ""
    model = ""
    price = 0

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
    
phone1 = mobile("Samsung", "Galaxy", 349)
phone2 = mobile("Apple", "Iphone 12", 899)
print(phone1)
print(phone2)
        