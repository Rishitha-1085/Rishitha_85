n = int(input())
while n >= 10:   
    sd = 0
    temp = n     
    while temp != 0:
        r = temp % 10
        sd += r
        temp = temp // 10
    n = sd      
print(n)
