'''write a program to find the factorial of a given number by using recursion
1ton multiplication happens
'''

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1) #recursive calling

n=int(input())
f=fact(n) #calling func
print(f)


'''
# Non Recursion program
n=int(input())
f=1
while n>=1:
    f*=n
    n-=1
print(f)
'''