from sys import stdin
readline = stdin.readline
def fab(a):
    a.sort(reverse=True)
    return a[0] + a[1]
s = list(map(int,readline().split()))
print(fab(s))

         
