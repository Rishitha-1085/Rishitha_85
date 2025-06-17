size=int(input("ENTER THE SIZE OF LIST:"))
list=[]
unique_list=[]
for i in range(size):
    temp=int(input(f"ENTER THE INTEGER VALUE AT {i} INDEX POSITION:"))
    list.append(temp)
print(f"USER ENTERED LIST:{list}")
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f"unique list :{unique_list}")
