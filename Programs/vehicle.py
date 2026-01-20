class Vehicle():
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(self.brand,
        self.speed)

class Car(Vehicle):
    def __init__(self,brand,speed,seats):
        super().__init__(brand,speed)
        self.seats = seats

    def display_info(self):
        print(self.brand,
        self.speed,self.seats)

class Bike(Vehicle):
    def __init__(self,brand,speed,engine_cc):
        super().__init__(brand,speed)
        self.engine_cc = engine_cc

    def display_info(self):
        print(self.brand,
        self.speed,self.engine_cc)    


vehicle_obj = Vehicle("Honda", 120)
car_obj = Car("Tesla" , 110 , 5)
bike_obj = Bike("Skoda" , 110 , 4)

vehicle_obj.display_info()
car_obj.display_info()
bike_obj.display_info()





