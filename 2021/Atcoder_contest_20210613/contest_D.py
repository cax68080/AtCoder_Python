from sys import stdin
readline = stdin.readline
def fab():
    n,q = map(int,readline().split())
    a = list(map(int,readline().split()))
    s = []
    for i in range(q):
        k = int(readline())
        for j in range(n):
            if k >= a[j]:
                k += 1
        s.append(k)
        k = 0
    for i in s:
        print(i)
        
fab()
