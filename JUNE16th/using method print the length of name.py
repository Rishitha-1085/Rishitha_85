#using method print the length of name

class person:
    def __init__(se,name,age):    #parameterized constructor
        se.name=name   
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def lengthprinting(self):
        print(len(self.name))
    
p1=person('kiran',40)    
p2=person('sandeep krishna',14)
p1.printing() 
p2.printing()
p1.lengthprinting() 
p2.lengthprinting()

