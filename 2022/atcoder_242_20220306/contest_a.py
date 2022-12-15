from sys import stdin
readline = stdin.readline
def fab(a,b,c,x):
    result = 0.0
    s = b - a
    if x <= a:
        result = 1.0
    elif a < x <= b:
        result = c /s
    else:
        result = 0.0
    return(result)
a,b,c,x = map(int,readline().split())
print(fab(a,b,c,x))
