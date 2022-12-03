from sys import stdin
readline = stdin.readline
def fab(s,a,b):
    result = s[0:a - 1] + s[b - 1] + s[a:b - 1] + s[a - 1] + s[b:]
    return result
s = str(readline())
a,b = map(int,readline().split())
print(fab(s,a,b))
