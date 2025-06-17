#staticmethod created using static method

class mathematics:
    def addnumbers(x,y):
        return x+y
m=staticmethod(mathematics.addnumbers)
print(m(4,44))


#staticmethod created using decorator

class mathematics:
    @staticmethod
    def addnumbers(x,y):
        return x+y
print(mathematics.addnumbers(33,88))
