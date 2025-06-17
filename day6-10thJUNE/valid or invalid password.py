str=input("enter the password: ")
digit_count=0
alph_count=0
specialchar=0
for ch in str.lower():
    if ch.isdigit():
        digit_count+=1
    elif ch.isalpha():
        alph_count+=1
    else:
        specialchar+=1
if specialchar!=0 and digit_count!=0 and alph_count!=0:
    print("VALID PASSWORD ")
else:
    print("INVALID PASSWORD ")
        
