#print sample IDs like LAB2025-017, and you need to generate the next 5
#Take a starting ID and create a list of the next n IDs
#enter the lab sample Id: LAB2025-017
#enter the no.of IDs you have to generate:5
#output: [LAB2025-018,LAB2025-019,LAB2025-020,LAB2025-021,LAB2025-022]



sample_prefix=int(input("Enter the sample prefix: "))
sample_format=""

n=int(input("Enter the Number of IDs you have to generate: "))
list=[]
for i in range(0,n):
    sample_format=(f"LAB2025-0{sample_prefix+1}")
    list.append(sample_format)
    sample_prefix+=1
print(list)
