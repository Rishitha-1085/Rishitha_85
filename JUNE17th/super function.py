class base:
    def __init__(self):
        self._a=32
        print(self._a)
        
class derived(base):
    def __init__(self):
        super().__init__()
        print(self._a+2)
        
class derived1(derived):
    def __init__(self):
        super().__init__()
        print(self._a+3)

       
x=derived1()

