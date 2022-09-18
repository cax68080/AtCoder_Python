from sys import stdin
readline = stdin.readline
def fab(n,p,list_a):
    result = 0
    for i in range(n):
        if list_a[i] < p:
            result += 1
    return result 
n,p = map(int,readline().split())
list_a = list(map(int,readline().split()))
print(fab(n,p,list_a))
