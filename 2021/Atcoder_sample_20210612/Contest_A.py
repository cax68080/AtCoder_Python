from sys import stdin
import re
readline = stdin.readline
def fab(s):
    a = list(s)
    h = 0
    t = 0
    n = 0
    for i in range(len(a)):
        if re.match('\d',a[i]):
            if i == 0:
                h = int(a[i]) * 100
            elif i == 1:
                t = int(a[i]) * 10
            else:
                n = h + t + int(a[i])
            result =  n * 2
        else:
            result = "error"
            break
    return result
l = str(readline()).replace('\n','')
print(fab(l))
