# METHOD RESOLUTION ORDER 

class A:
    def myname(self):
        print("I am a Class A")
class B(A):
    def myname(self):
        print("I am a Class B")
class C(A):
    def myname(self):
        print("I am a Class C")

        #classes ordering
class D(C,B):
    pass
d=D()
d.myname()


print(D.__mro__)  #_mro_ keyword
print(D.mro())    # mro  function

c=C()
print(C.mro())
