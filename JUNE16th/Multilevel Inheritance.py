#MULTI LEVEL INHERITANCE

class base:
    def __init__(self):
        self._a=32  #protected variable
        print(self._a)

class derived(base):
    def __init__(self):
        base.__init__(self) #invoking
        print(self._a+2)
class derived1(derived):
    def __init__(self):
        derived.__init__(self) 
        print(self._a*2)

x=derived1()  #MULTILEVEL INHERITANCE

