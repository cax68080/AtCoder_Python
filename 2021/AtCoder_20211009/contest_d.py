from sys import stdin
readline = stdin.readline
def fab(n,list_a,list_b):
    t = 1
    for i in range(n):
        j = 0
        m = 0
        s = list_b[i] - list_a[i] + 1
        t = t * s
        if i > 0 and list_a[i] < list_b[i-1]:
            k = list_b[i-1] - list_a[i]
            for p in range(1,k+1):
                j += p
        if i > 0 and list_b[i] < list_a[i - 1]:
            l = list_a[i-1] - list_b[i] 
            for q in range(1,l+1):
                m += q
        t = t - (j + m)
    result = t % 998244353
    return result
n = int(readline())
list_a = list(map(int,readline().split()))
list_b = list(map(int,readline().split()))
print(fab(n,list_a,list_b))
