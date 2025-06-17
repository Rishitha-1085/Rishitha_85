# Normal METHOD

class person:
    def __init__(se,name,age):    #special method-constructor
        se.name=name   #static variable
        se.age=age
    def printing(self):
        print(self.name,self.age)
    
p1=person('kiran',40)    
p2=person('sandeep',41)
p1.printing() #calling printing function through p1
p2.printing()
