
import sys
sys.setrecursionlimit(100)
def vignan():
    global i
    i+=1
    print(i)
    vignan() #recursive call

i=0
vignan() #calling function