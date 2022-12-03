from sys import stdin
readline = stdin.readline
def fab(n,list_s,t):
    s_max = max(list_s)
    s_min = min(list_s)
    cnt = 0
    flg = 0
    while flg == 0:
        if t < s_min:
            t *= 2
        else:
            flg = 1
    for i in range(n):
        if t > s_max:
            cnt += 1
            break
        elif t < list_s[i]:
            t *= 2
            cnt += 2
        elif t > list_s[i]:
            continue
        else:
            continue
    return cnt
n = int(readline())
list_s = list(map(int,readline().split()))
list_s.sort(key=None,reverse=False)
t = int(readline())
print(fab(n,list_s,t))