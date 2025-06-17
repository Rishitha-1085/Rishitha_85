#SINGLE INHERITANCE:

class father:
    def __init__(self,name):  #self refers to obj ie x
        self.name=name
    def show(self):
        print(self.name)      #father name
class son(father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)      #printing son name

x=father('Nagarjuna')
x.show()
y=son('Akhil')
y.show1()
#Inheritance
y.show()

