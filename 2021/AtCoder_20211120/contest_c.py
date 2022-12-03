from sys import stdin
readline = stdin.readline
def fab(n,k,list_p):
    list_cnt = sorted(list_p,reverse=True)
    k = k - 1
    for i in list_p:
        chk = i + 300
        if list_cnt[k] <= chk:
            print("Yes")
        else:
            print("No")


n,k = map(int,readline().split())
list_p = []
for i in range(n):
    list_cnt = list(map(int,readline().split()))
    list_p.append(sum(list_cnt))
fab(n,k,list_p)