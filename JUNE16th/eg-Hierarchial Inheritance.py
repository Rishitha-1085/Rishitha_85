# Hierarchial Inheritance

class father:
    fathername='' #static variable
    def Father(self): #method   default constructor present
        print(self.fathername)

class mother:
    mothername='' 
    def Mother(self): 
        print(self.mothername)

class son1(father,mother):
    son1name=''
    def Son1information(self):
        print(self.fathername)  #inheritance
        print(self.mothername)
        print(self.son1name)

class son2(father):
    son2name=''
    def Son2information(self):
        print(self.fathername)  
        print(self.son2name)


s1=son1()
s1.son1name='Lava'
s1.fathername="Ram"
s1.mothername="Sita"
#s1.Son1information()

s2=son2()
s2.fathername="Ram"
s2.son2name='Kusha'
#s2.Son2information()

s1.Father()
s1.Mother()
s2.Father()
