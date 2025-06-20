'''
program to count the uppercase alphabet,lowercase alphabet,digit and 
special symbols present in given string
'''
s1="Vignan College Bt @ 2025"
uc=0
lc=0
di=0
sc=0
for ch in s1:
    if ch.isalpha() and ch.islower():
        lc+=1
    elif ch.isalpha() and ch.isupper():
        uc=uc+1
    elif ch.isdigit():
        di+=1
    else:
        sc+=1


print("uc:",uc)
print("lc:",lc)
print("digitscount: ",di)
print("sc: ",sc)
