
def a1():
    a=5   #local variable
    c=a+b
    print(c)
    print(a)
    print(id(a))

def a2():
    a=10
    print(a)
    print(id(a)) #address

b=15    #global variable
print(b)
print(id(b))
a1()#calling function
a2()
