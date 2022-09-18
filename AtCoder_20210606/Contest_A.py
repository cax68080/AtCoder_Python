def fib(x,y):
    if x == y:
        return x
    elif (x == 0) & (y == 1):
        return 2
    elif (x == 0) & (y == 2):
        return 1
    elif (x == 1) & (y == 0):
        return 2
    elif (x == 1) & (y == 2):
        return 0
    elif (x == 2) & (y == 0):
        return 1
    elif (x == 2) & (y == 1):
        return 0
    else:
        return 0
a,b = map(int,input().split())
print(fib(a,b))

    
        