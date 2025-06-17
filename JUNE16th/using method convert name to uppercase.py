#using method converting name to uppercase
class person:
    def __init__(se,name,age):    
        se.name=name   
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def uppercaseconversion(self):
        x=self.name
        print(x.upper())
    
p1=person('kiran',40)    
p2=person('sandeep',14)
p1.printing() 
p2.printing()

p1.uppercaseconversion()
p2.uppercaseconversion()
