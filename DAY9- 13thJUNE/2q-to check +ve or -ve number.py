def number(Num):
    if(Num==0):
        print(f"{Num} is Zero")
    elif(Num>0):
        print(f"{Num} is positive")
    else:
        print(f"{Num} is negative")

Num=int(input("Enter a number: "))
number(Num)
