# getattr(),setattr(),hasattr()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('Anil',36)
print(getattr(p1,'name')) #print(p1.name)
print(getattr(p1,'age'))   #print(p1.age)

setattr(p1,'age',40)    
print(getattr(p1,'age'))
print(hasattr(p1,'age'))
print(hasattr(p1,'id'))

print(hasattr(p1,'name'))
