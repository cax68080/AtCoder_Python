from sys import stdin
readline = stdin.readline
def fab(a,b):
    if len(a) > len(b):
        cnt = len(b) * -1 - 1
    else:
        cnt = len(a) * -1 - 1
    result = "Easy"
    for i in range(-1,cnt,-1):
        if int(a[i])+ int(b[i]) >= 10:
            result = "Hard"
            break
    return result
a,b = map(str,readline().split())
print(fab(a,b))
