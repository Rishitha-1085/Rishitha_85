#non parameterized constructor

class person:
    count=0    
    def __init__(self):
        person.count+=1    #count represent no of objects of class

p1=person()
print(p1.count)
p2=person()
print(p2.count)
p3=person()
print(person.count)
        
