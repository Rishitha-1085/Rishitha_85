n=int(input())
for i in range(1, n + 1,1):
        for s in range(n-i,0,-1):
            print(" ",end='')
        for d in range(1,i+1,1):
            print('#',end='')
        print()