'''write a program to find the factorial of a given number by using recursion
n to 1 multiplication happens
'''
'''
def fact(n,a,b):
    if n==0 or n==1:
        return b
    else:
        n-=1
        return fact(n,a,b*n) 

n=int(input())
result = fact(n, 1, n)
print(result)
'''

def fact(x,n,a,b):
    if(x==a):
        print(b)
    else:
        n-=1
        a+=1
        return fact(x,n,a,b*n)
n=int(input())
if n==0 or n==1:
    print(1)
else:
    fact(n,n,1,n)

