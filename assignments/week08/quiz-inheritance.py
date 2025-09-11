""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"Brand:{self.brand},Model:{self.model,Year:{self.year}}"
class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors=number_of_doors
    def get_info(self):#overriding method ควรจำ
        return f"Brand:{self.brand},Model:{self.model},Year:{self.year},Number Of Doors:{self.number_of_doors}"
car=Car("Yamaha","GeneretionX",2077,6)
print(car.get_info())