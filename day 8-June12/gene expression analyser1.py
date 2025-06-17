n=int(input("Enter the no.of gene expression data values: "))
expression_values=[]
genedata=[]
for i in range(n):
    value=float(input(f"Enter expression values:"))
    expression_values.append(value)
for value in expression_values:
    if value<5:
        genedata.append("underexpressed")
    elif 5<value<15:
        genedata.append("Normal")
    else:
        genedata.append("Overexpressed")
print(genedata)
