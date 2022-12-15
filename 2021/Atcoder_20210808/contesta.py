from sys import stdin
readline = stdin.readline
def fab(a,b):
    result = a ^ b
    return result
a,b = map(int,readline().split())
print(fab(a,b))