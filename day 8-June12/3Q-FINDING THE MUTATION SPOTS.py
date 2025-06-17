#comparing to DNA sequence and finding mutations
#compare 2 strings of the same length and print the position(indices) where sequence differ
#seq1=AAGCTCGA #seq2="AACCTAGA" output:[2,6]



seq1=input("Enter the First DNA Sequence: ")
seq2=input("Enter the Second DNA Sequence: ")

if len(seq1)!=len(seq2):
    print("Enter the sequences of same length")
else:
    indices=[]
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            indices.append(i)
    print(indices)
    
