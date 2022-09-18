from sys import stdin
readline = stdin.readline
def fab(x,y):
    if y - x > 0:
        s = y - x
        m = s // 10
        n = s % 10
        if n == 0:
            result = m
        else:
            result = m + 1
    else:
        result = 0
    return result

x,y = map(int,readline().split())
print(fab(x,y))
