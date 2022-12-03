from sys import stdin
readline = stdin.readline
def fab(n,list_a):
    result = ""
    gld = 1
    for i in range(n):
        if gld == 1 and i + 1 < n and list_a[i] > list_a[i+1]: 
            gld = 0
            result = result + "1 "
        elif gld == 0 and i + 1 < n and list_a[i] < list_a[i+1]:
            gld = 1
            result = result + "1 "
        elif gld == 0 and i == n - 1:
            gld = 1
            result = result + "1 "
        else:
            result = result + "0 "
    return result 
n = int(readline())
list_a = list(map(int,readline().split()))
print(fab(n,list_a))
