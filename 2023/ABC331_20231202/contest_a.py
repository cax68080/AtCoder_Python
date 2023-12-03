from sys import stdin
readline = stdin.readline
m,d = map(int,readline().rstrip("\n").split())
yy,mm,dd = map(int,readline().rstrip("\n").split())
if dd == d:
    dd = 1
    if mm == m:
        mm = 1
        yy += 1
    else:
        mm += 1
else:
    dd += 1
print(str(yy) + " " + str(mm) + " " + str(dd))