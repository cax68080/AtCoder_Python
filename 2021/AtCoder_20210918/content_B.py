from sys import stdin
readline = stdin.readline
def fab(a,t):
    result = ""
    for i in range(len(t)):
        l = int(t[i]) - 1
        result = result + a[l]
    return result
a = []
for _ in range(3):
    s = str(readline()).rstrip('\n')
    a.append(s)
t = str(readline()).rstrip('\n')
print(fab(a,t))

