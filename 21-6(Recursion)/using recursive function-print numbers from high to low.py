
'''write a recursive program to print the numbers from  high(a) to low(b) ie 10 to 5'''

def rhl(x,y):
    if(x>=y):
        print(x)
        x-=1
        rhl(x,y) #recursive calling statement 


a,b=map(int,input().split())
rhl(a,b) #calling function
