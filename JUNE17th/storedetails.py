class store:
    def __init__(self, name,itemscount):
        self.name = name
        self.itemscount =itemscount

    def calculation(self):
        x=self.itemscount
        tp=0
        for i in range(x):
            p=int(input(f"enter the prices of item{i+1}: "))
            tp+=p
        return tp
    def discount(self,amount):
        print(amount-amount*0.2)

name=input("Enter the name: ")
itemscount=int(input("Enter no of items: "))
c1=store(name,itemscount)
tp=c1.calculation()
if(tp>=200):
    c1.discount(tp) #calling function  
else:
    print(tp)
