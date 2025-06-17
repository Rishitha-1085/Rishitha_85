#you have got a prt seq made upof aa and a dictionary of their mwt. we have to find the total weight of the protein
# loop through the prt string , get the weight of each aa,calculate the total
# input: "ACDEF" output: Total weight=583.7(based on given weights)

aminoacids_weight={
    'A':89.1,
    'C':121.2,
    'D':133.1,
    'E':147.1,
    'F':165.2,
    'G':75.1,
    'H':155.2,
    'I':131.2,
    'K':146.2,
    'L':131.2,
    'M':149.2,
    'N':132.1,
    'P':115.1,
    'Q':146.2,
    'R':174.2,
    'S':105.1,
    'T':119.1,
    'V':117.1,
    'W':204.2,
    'Y':181.2
}
protein=input("ENTER THE PROTEIN SEQUENCE VALUE: ")
total=0
for ch in protein:
    if ch in aminoacids_weight:
        total+=aminoacids_weight[ch]
    else:
        print("Enter the valid protein sequence")

print("Total weight = ",total)
