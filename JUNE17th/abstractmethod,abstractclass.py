#ABSTRACTION-abstract method,abstract class

from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod   #convert normal method to abstractmethod @ means decorate
    def mileage(self):
        pass        #pass-empty method


class tesla(car):
    def mileage(self):
        print("mileage is 20kmph")

class suzuki(car):
    def mileage(self):
        print("mileage is 12kmph")
t1=tesla()
t1.mileage()
s1=suzuki()
s1.mileage()
