#2nd logic 
def Is_prime(Num):
    count=0
    for i in range(2,Num//2+1):
        if(Num%i==0):
            count+=1
    if(count==0):
        print(f"{Num} is prime")
    else:
        print(f"{Num} is Not prime")

Num=int(input("Enter a number: "))
Is_prime(Num)
