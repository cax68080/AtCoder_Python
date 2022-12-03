from sys import stdin
readline = stdin.readline
def fib():
    n = int(readline())
    l = list(map(int,readline().split()))
    cnt = 0
    for i in range(n):
        if l[i] > 10:
            cnt = cnt + (l[i] - 10)
    return cnt
print(fib())

