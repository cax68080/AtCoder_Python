from sys import stdin
readline = stdin.readline
def fab(x):
    result = round(x + 0.0001)
    return result
x = float(readline())
print(fab(x))
