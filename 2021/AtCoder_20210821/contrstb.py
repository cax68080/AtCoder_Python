from sys import stdin
readline = stdin.readline
def fab(n):
    k = 1
    while cnt < n:
        cnt = 2 ** k
        if cnt < n:
            result = cnt
            k += 1
    return result
n = int(readline())
print(fab(n))