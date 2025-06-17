# ENCAPSULATION

class base:                 #class
    def __init__(self):     #method
        self.__a=32         #private data-use only in this class
        print(self.__a)
        
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)    #private data cannot acess in this class
'''       
d1=derived()  -this line gives error bcz the private data cannot acess in derived class
'''

b1=base()
'''
print(b1.__a)   -this is an error bcz the private data is securied 
'''
