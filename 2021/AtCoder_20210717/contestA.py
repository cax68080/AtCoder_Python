from sys import stdin
readline = stdin.readline
def fab(n,a,x,y):
    if n <= a:
        total = x * n
    else:
        total = (x * a) + (y * (n - a))
    return total
n,a,x,y = map(int,readline().split())
print(fab(n,a,x,y))
