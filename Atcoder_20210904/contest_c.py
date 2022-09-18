from sys import stdin
readline = stdin.readline
n = int(readline())
a = [0] + list(map(int,readline().split()))
q = [-1] * (n+1)
result = ''
for i in range(1,n+1):
    q[a[i]] = i
print(' '.join(map(str,q[1:])))


