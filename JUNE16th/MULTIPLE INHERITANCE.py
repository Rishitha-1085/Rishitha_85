#MULTIPLE INHERITANCE:

class father:
    fathername='' #static variable
    def Father(self): #method   default constructor present
        print(self.fathername)

class mother:
    mothername='' 
    def Mather(self): 
        print(self.mothername)



class son1(father,mother):
    son1name=''
    def Son1information(self):
        print(self.fathername)  #inheritance
        print(self.mothername)
        print(self.son1name)


s1=son1()
s1.son1name='Lava'
s1.fathername="Ram"
s1.mothername="Sita"

s1.Son1information()
