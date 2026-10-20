# prgm to demonstrate the concept of constructor & destructor


class Student:
  def __init__(self,name):
    self.name = name
    print("Constructor Called...!")
    print("Student Name is ",self.name)
    print("Object created")
    
    
  def __del__(self):
    print("Destructor Called....!")
    print("Object deleted")
    
  

    
s1 = Student("Naruto Utsumaki")
del s1
