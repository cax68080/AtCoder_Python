from sys import stdin
readline = stdin.readline
def fab(x):
    if x > 0 and x % 100 == 0:
        return "Yes"
    else:
        return "No"
x = int(readline())
print(fab(x))