#operator overloading-class,obj

class A:
    def __init__(self,a):
        self.a=a
    #adding two objects
    def __add__(self,o):
        return self.a+o.a
ob1=A(1)
ob2=A(1)
print(ob1+ob2)
ob3=A("Geeks")
ob4=A("For")
print(ob3+ob4)
