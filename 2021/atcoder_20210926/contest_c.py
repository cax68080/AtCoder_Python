from sys import stdin
readline = stdin.readline
def fab(n,alist,x):
    a = 0
    for i in alist:
        a += i
    s = x // a
    t = x % a
    k = a * s
    for i in range(len(alist)):
        k += alist[i]
        if k > x:
            l = i + 1
            break
    result = n * s + l
    return result

n = int(readline())
alist = list(map(int,readline().split()))
x = int(readline())
print(fab(n,alist,x))
