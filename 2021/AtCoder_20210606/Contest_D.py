from sys import stdin
readline = stdin.readline
def fib():
    n = int(readline())
    t = list(map(int,readline().split()))
    t.sort(key=None,reverse=True)
    c1 = 0
    c2 = 0
    for i in range(n):
        if c1 <= c2:
            c1 = c1 + t[i]
        else:
            c2 = c2 + t[i]
    if c1 >= c2:
        return c1
    else:
        return c2    
    
print(fib())


