#  prgm to create a vehicle class with maximum speed,mileages as instant attribute



class Vehicle:
  def __init__(self,name,max_speed,mileage):
    self.name = name
    self.speed = max_speed
    self.mileage = mileage
    
car = Vehicle("BMW",120,23)

print("Model: ", car.name)
print("Maximum Speed: ", car.speed ,"km/hrs")
print("Mileage: ", car.mileage ,"km/lrs")
