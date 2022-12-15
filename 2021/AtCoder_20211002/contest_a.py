from sys import stdin
readline = stdin.readline
def fab(a,b):
    ma = 1
    mb = 1
    for i in range(a):
        ma = ma * 32
    for i in range(b): 
        mb = mb * 32
    result = ma // mb
    return result
a,b = map(int,readline().split())
print(fab(a,b))
