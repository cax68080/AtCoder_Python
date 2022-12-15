from sys import stdin
readline = stdin.readline
def fab():
    n = int(readline())
    c = list(map(int,readline().split()))
    c.sort()
    for i in range(n):
        if i == 0:
            cnt = c[i]
        else:    
            cnt = cnt *  (c[i] - i ) % (10**9 + 7)
    return cnt
print(fab())


