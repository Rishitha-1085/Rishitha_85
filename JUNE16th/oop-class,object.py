#object oriented programming- class,object

class person:
    age=36    #age data is static variable-bcz it can be used by total objects of class

    
p1=person()  #object creation
print(p1.age)

p2=person()
print(p2.age)

print(person.age)
