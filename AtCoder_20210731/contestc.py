from sys import stdin
readline = stdin.readline
def fab():
    n,m = map(int,readline().split())
    a = list(map(int,readline().split()))
    b = list(map(int,readline().split()))
    for i in range(n):
        for k in range(m):
            if i == 0 and k ==0:
                result = abs(a[i]-b[k])
            else:
                if result > abs(a[i]-b[k]):
                    result = abs(a[i]-b[k])
    return result
print(fab())