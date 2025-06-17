size=int(input("ENTER THE SIZE OF LIST:"))
toy_names=[]
unique_toys=[]
for i in range(size):
    temp=input(f"ENTER THE INTEGER VALUE AT {i} INDEX POSITION:")
    toy_names.append(temp)
print(f"LIST OF TOYS:{toy_names}")
for i in toy_names:
    if i not in unique_toys:
        unique_toys.append(i)
print(f"unique toys list :{unique_toys}")
unique_toys.sort()
print("sorted final toys list:")
print(unique_toys)
