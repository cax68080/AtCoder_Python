from sys import stdin
readline = stdin.readline
def fab(n,list_a):
    list_k = []
    cnt = 0
    result = 0
    for i in list_a:
        cnt = cnt + i
        if cnt >= 360:
            cnt = cnt - 360
        list_k.append(cnt)
    list_k.append(0)
    list_k.append(360)
    list_k.sort(key=None,reverse=False)
    for i in range(len(list_k)):
        if i == 0:
            continue
        else:
            d = list_k[i] - list_k[i - 1]
        if result < d:
            result = d
    return result
    
n = int(readline())
list_a = list(map(int,readline().split()))
print(fab(n,list_a))
    