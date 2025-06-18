#conversion of decimal to binary
n=int(input("ENTER A NUMBER: "))
x=bin(n)
print(x)
print(type(x))

#conversion of binary to decimal
da=int(x,2) #(data to convert,base of data)
print(da)

#conversion of decimal to octal
n=int(input("ENTER A NUMBER: "))
x=oct(n)
print(x)
print(type(x))

#conversion of octal to decimal
da=int(x,8) #(data to convert,base of data=8)
print(da)




#conversion of decimal to hexadecimal
n=int(input("ENTER A NUMBER: "))
x=hex(n)
print(x)
print(type(x))

#conversion of hexadecimal to decimal
da=int(x,16) 
print(da)
