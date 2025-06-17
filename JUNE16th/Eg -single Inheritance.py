#eg Single Inheritance

class base:
    def __init__(self):
        self._a=32  #protected variable
        print(self._a)

class derived(base):
    def __init__(self):
        base.__init__(self) #invoking
        print(self._a+2)

x=base()
y=derived()

print(x._a)
print(y._a)
