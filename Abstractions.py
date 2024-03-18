##Abstractions

from abc import ABC , abstractmethod

class India(ABC):
   # @abstractmethod
    def Ak47(self):
        pass        
   
class Jammu_kasmir(India):
    # abstractmethod override
    def Ak47(self):
        print("this is jammu&kasmir gun")

        
class Rajasthan(India):
    
    # abstractmethod override

    def Ak47(self):
        print("this is Ak47 gun from Rajasthan")
class Nepalborder(India):
    
    # abstractmethod override

    def Ak47(self):
        print("this is nepalboreder gun Ak47 gun")

    
obj_one = Jammu_kasmir()
obj_two = Rajasthan()
obj_three = Nepalborder()

obj_one.Ak47()
obj_two.Ak47()
obj_three.Ak47()

