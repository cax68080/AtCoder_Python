from sys import stdin
readline = stdin.readline
def fab(x,n,s):

x = ""
x = str(readline())
x = "0" + x
n = int(readline())
s = [n]
for _ in range(n):
    s.append(str(readline()))
fab(x,n,s)