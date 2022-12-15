from sys import stdin
readline = stdin.readline
def fab(y):
    if 0 <= y <= 2:
        result = "-"
    elif 3 <= y <= 6:
        result = ""
    else:
        result = "+"
    return result
x,y = map(int,readline().split('.'))
print(str(x) + fab(y))