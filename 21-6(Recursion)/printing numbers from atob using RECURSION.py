''' write a recursive program to print the numbers from low to high ie 5 to 10
low to high <,<=
high to low >,>=
'''
#NON RECURSION PROGRAM:
'''
a,b=map(int,input().split())
while a<=b:
    print(a)
    a+=1
'''


def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y) #recursive calling statement


a,b=map(int,input().split())
rlh(a,b) #calling function
