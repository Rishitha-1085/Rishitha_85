size=int(input("enter the range of numbers: "))
list=[]
for i in range(size):
    value=int(input(f"enter the number on {i} index: "))
    list.append(value)
print("list of numbers: ",list)
list.sort()
print("Sorted list of numbers: ",list)
print("maximum numbers: ",list[-1])
