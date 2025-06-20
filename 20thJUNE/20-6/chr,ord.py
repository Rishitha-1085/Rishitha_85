s=input()
uc,lc,dc,sc=0,0,0,0
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        uc+=1
    elif ord(i)>=97 and ord(i)<=122:
        lc+=1
    elif ord(i)>=48 and ord(i)<=57:
        dc+=1
    else:
        sc+=1
print("uc:",uc)
print("lc:",lc)
print("dc: ",dc)
print("sc: ",sc)