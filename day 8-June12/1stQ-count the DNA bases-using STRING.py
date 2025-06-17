#checking if a string has only validbases(A,T,G,C), count of each bases
#output: {'A':5,'T':4,'G':2,'C':2}


dna=input("Enter a DNA bases: ")
for ch in dna:
    if ch in "ATGC":
        A=dna.count('A')
        T=dna.count('T')
        G=dna.count('G')
        C=dna.count('C')
print({'A':A,'T':T,'G':G,'C':C})

        
