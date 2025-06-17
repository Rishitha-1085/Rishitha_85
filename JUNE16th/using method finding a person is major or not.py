#check whether the person is major or not using method

class person:
    def __init__(se,name,age):    
        se.name=name   
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self):
        if(self.age>18):
            print("person is major")
        else:
            print("MINOR")
        
    
p1=person('kiran',40)    
p2=person('sandeep',14)
p1.printing() 
p2.printing()

p1.decide()
p2.decide()
