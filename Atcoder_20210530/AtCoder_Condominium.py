from sys import stdin
readline = stdin.readline
def fab(fl,rm):
    t = 0
    for i in range(1,fl + 1):
        for j in range(1,rm + 1):
            t += int(str(i) + "0" + str(j))
    return t
n,k = map(int,readline().split())
print(fab(n,k))


