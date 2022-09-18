from sys import stdin
readline = stdin.readline
def fab():
    n,x = map(int,readline().split())
    a = list(map(int,readline().split()))
    total = 0
    cnt = 1
    for i in range(n):
        if cnt % 2 == 0:
            total += a[i] -1
        else:
            total += a[i]
        cnt += 1
    if total <= x:
        result = "Yes"
    else:
        result = "No"
    return result
print(fab()) 
