def Is_primenumber(Num):
    count=0
    if Num>1:
        for i in range(1,Num+1):
            if(Num%i==0):
                count+=1
        if(count==2):
            print(f"{Num} is prime")
        else:
            print(f"{Num} is Not prime")

    else:
        print(f"{Num} is Not prime")

Num=int(input("Enter a number: "))
Is_primenumber(Num)



