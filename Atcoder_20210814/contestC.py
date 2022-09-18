from sys import stdin
readline = stdin.readline
def fab():
    n = int(readline())
    s = list(map(int,readline().split()))
    t = list(map(int,readline().split()))
    result = []
    r = 0
    for i in range(n):
        if i == 0:
            result.append(t[i])
            r = t[i]
        else:
            r = s[i - 1]
            if t[i] > r:
                result.append(r)
            else:
                result.append(t[i])
    #result.sort()
    for k in range(n):
        print(result[k])
fab()
        