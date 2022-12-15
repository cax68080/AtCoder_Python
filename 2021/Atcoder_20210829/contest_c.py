from sys import stdin
readline = stdin.readline
def fab(n):
    if n % 2 == 0:
        m = n / 2 
    else:
        m = (n - 1) / 2
    for i in range(120):
       if i == 0:
           result = "A"
           cnt = 1
       if cnt < m:
           cnt = cnt * 2
           result = result + "B"
       elif cnt < n:
           cnt = cnt + 1
           result = result + "A"
       else:
           continue
    return result
n = int(readline())
print(fab(n))


