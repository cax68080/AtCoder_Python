from sys import stdin
readline = stdin.readline
def fab(a,b):
    total = 0
    total = b - a + 1
    if total < 0:
        total = 0
    return total
a,b = map(int,readline().split())
print(fab(a,b))