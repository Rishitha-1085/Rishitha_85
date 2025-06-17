#label each gene "underexpressed"(<5) "Normal"(5 to 15)  "Overexpressed"(>15)
#loop through a list and assign the correct label to each number.
#input:[3.2,5.5,12.4,16.7,2.1]
#output:["underexpressed","Normal","Normal","Overexpressed","underexpressed"]

expression_values=list(map(float,input("Enter the no.of gene expression data values: ").split(",")))
genedata=[]
for value in expression_value:
    if value<5:
        genedata.append("underexpressed")
    elif 5<value<15:
        genedata.append("Normal")
    else:
        genedata.append("Overexpressed")
print(genedata)
