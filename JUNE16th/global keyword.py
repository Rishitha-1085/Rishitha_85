#Global keyword- to modify the global variable data in a function.

def a1():
    global a
    a=a*a
    print(a)

a=5
print(a)
a1()
print(a)

'''
def a1():
    b=a*a
    print(b)

a=5
a1()
'''
