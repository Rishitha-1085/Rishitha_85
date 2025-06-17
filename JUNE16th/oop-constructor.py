#Constructor:

class person:
    def __init__ (self,name,age):    #2 parameters-name,age
        self.name=name    #instant variable-bcz name,age data depend on object
        self.age=age    
p1=person('kiran',40)    #object creation
p2=person('sandeep',41)
print(p1.age,p1.name)
print(p2.age,p2.name)
