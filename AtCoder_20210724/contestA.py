from sys import stdin
readline = stdin.readline
def fab(a,b):
    result = (a - b) /3 + b
    #result = int(result)
    return result
a,b = map(int,readline().split())
print(fab(a,b))
