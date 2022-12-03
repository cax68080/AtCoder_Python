from sys import stdin
readline = stdin.readline
def fab(a,b):
    if a > 0:
        if b > 0:
            result = "Alloy"
        else:
            result = "Gold"
    else:
        if b > 0:
            result = "Silver"
    return result
a,b = map(int,readline().split())
print(fab(a,b))
