num = int(input("Enter the value of Num : "))
if((num>=100 and num<=999) or (num>=-999 and num<=-100)):
    print(f"{num} is  three Digit")
if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)):
    print(f"{num} is  four Digit")
else:
    print(f"{num} is not a 3 digit")
