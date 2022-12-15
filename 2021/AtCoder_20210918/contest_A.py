from sys import stdin
readline = stdin.readline
def fab(x):
    if x < 40:
        result = str(40 - x)
    elif x < 70:
        result = str(70 - x)
    elif x < 90:
        result = str(90 - x)
    else:
        result = "expert"
    return result
x = int(readline())
print(fab(x))
