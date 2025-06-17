food_item=['lays','choclate','icecream','pasta','oats']
prices=(20,50,20,120,60)
print(food_item)
order=input("enter your orders: ")
quantity=int(input("quantity: "))
bill=0
if (order in food_item):
    i=food_item.index(order)
    bill=bill+(quantity*prices[i])
    print(bill+(bill*0.18))
