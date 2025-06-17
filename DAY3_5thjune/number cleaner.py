size=int(input("Enter the range of List : "))
num=[]
temp=0
for i in range(size):
    value=int(input(f"enter the value at {i} index :"))
    num.append(value)
print(f"original list: {num}")
for i in range(size):
         if(num[i]<0):
             num[i]=0
print(f"updated list: {num}")         
for i in range(size):
         if(num[i]%3==0):
             print(num[i])
