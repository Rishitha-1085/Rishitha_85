'''
program to count the uppercase alphabet,lowercase alphabet,digit and 
special symbols present in given string
s1="Vignan College Bt @ 2025"
'''
#1st solution
import string
s=input()
uc,lc,dc,sc=0,0,0,0
d=string.digits
u=string.ascii_uppercase
l=string.ascii_lowercase
for i in s:
    if i in u:
        uc+=1
    elif i in l:
        lc+=1
    elif i in d:
        dc+=1
    else:
        sc+=1
print("uc:",uc)
print("lc:",lc)
print("digitscount: ",dc)
print("sc: ",sc)

#2nd solution
s=input()
uc,lc,dc,sc=0,0,0,0
for i in s:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
    elif i.isnumeric():
        dc+=1
    else:
        sc+=1
print("uc:",uc)
print("lc:",lc)
print("dc: ",dc)
print("sc: ",sc)

#3rd solution
s=input()
uc,lc,dc,sc=0,0,0,0
for i in s:
    if i>='A' and i<='Z':
        uc+=1
    elif i>='a' and i<='z':
        lc+=1
    elif i>='0' and i<='9':
        dc+=1
    else:
        sc+=1
print("uc:",uc)
print("lc:",lc)
print("dc: ",dc)
print("sc: ",sc)