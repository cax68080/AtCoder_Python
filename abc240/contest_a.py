from sys import stdin
#from math import abs
readline =stdin.readline
def fab(a,b):
    if abs(a - b) == 1 or abs(a - b) == 9:
        return "Yes"
    else:
        return "No"
a,b = map(int,readline().split())
print(fab(a,b))