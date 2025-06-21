'''  Tower of Hanoi
Only one disk can be moved at a time.
A disk can only be placed on top of a larger disk or an empty peg.
You want to move all disks from the source peg to the target peg.
'''

def toh(n,a,b,c):  #no.of disc , input tower,output,temporary
    if(n>0):
        toh(n-1,a,c,b)
        print(a,'->',c)
        toh(n-1,b,c,a)
n=int(input())
toh(n,'a','b','c')