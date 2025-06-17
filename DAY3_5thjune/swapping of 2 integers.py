#swapping of two integers
num1=10
num2=13
print(f"NUM1= {num1}")
print(f"NUM2= {num2}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#python method
num1,num2=num2,num1
print("AFTER SWAPPING")
print(f"NUM1= {num1}")
print(f"NUM2= {num2}")
#swapping of two integers  using third variable
temp=num1
num1=num2
num2=temp
print("AFTER SWAPPING")
print(f"NUM1= {num1}")
print(f"NUM2= {num2}")
#swapping of two integers without using third variable
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("AFTER SWAPPING")
print(f"NUM1= {num1}")
print(f"NUM2= {num2}")
