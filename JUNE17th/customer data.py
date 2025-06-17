'''
1.represent the name of the customer and the number of items purchased by the customer in the store using a class.
2.As per the no.of items read the prices and cal the total price
3.if the totalprice is >200 rupees provide a discount of 20% if not no discount
'''

class store:
    def __init__(self, name, noofitems):
        self.name = name
        self.noofitems = noofitems

    def calculation(self):
        x=self.noofitems
        tp=0
        for i in range(x):
            p=int(input(f"enter the prices of item{i+1}: "))
            tp+=p
        return tp
'''       
c1=store('kiran',4)
y=c1.calculation()  #stored return value
'''

name=input("Enter the name: ")
noofitems=int(input("Enter no of items: "))
c1=store(name,noofitems)
y=c1.calculation()
if(y>=200):
    print(y-y*0.2)
  
else:
    print(y)
    
