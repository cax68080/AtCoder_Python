from sys import stdin
readline = stdin.readline
def fab(n,k,a):
    s = n - (a - 1)
    t = k - s
    result = t % n
    if result == 0:
        result = n
    return result 
n,k,a = map(int,readline().split())
print(fab(n,k,a))
