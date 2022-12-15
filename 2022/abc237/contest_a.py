from sys import stdin
readline = stdin.readline
s = -2 ** 31
l = 2 ** 31
n = int(readline())
if s <= n < l:
    print("Yes")
else:
    print("No")
    
