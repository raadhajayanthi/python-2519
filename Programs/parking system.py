class Parkingsystem:
    def __init__(self,big,medium,small):
       self.big = big
       self.medium = medium
       self.small = small

    def addcar(self,cartype):
      if cartype == 1:
         if self.big > 0:
          self.big = self.big - 1
          return True
         else:
            print("no space")
      elif cartype == 2:
        if self.medium > 0:
         self.medium = self.medium - 1
         return True
        else:
            print("no space")
      elif cartype == 3:
        if self.small > 0:
         self.small = self.small - 1
         return True
        else:
         print("no space")
      else:
           print("no space") 
         
       

parkingsystem_obj = Parkingsystem(1,2,3)
print(parkingsystem_obj.addcar(1))
print(parkingsystem_obj.addcar(2))
print(parkingsystem_obj.addcar(3))

print(parkingsystem_obj.addcar(1))
print(parkingsystem_obj.addcar(2))
print(parkingsystem_obj.addcar(3))


print(parkingsystem_obj.addcar(1))
print(parkingsystem_obj.addcar(2))
print(parkingsystem_obj.addcar(3))