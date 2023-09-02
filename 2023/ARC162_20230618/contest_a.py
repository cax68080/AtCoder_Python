from sys import stdin
readline = stdin.readline
t = int(readline().rstrip("\n"))
for _ in range(t):
    n = int(readline().rstrip("\n"))
    list_p = list(map(int,readline().split()))
    #print(n)
    #print(list_p)
    cnt = 0
    jud = 0
    flg_jud = 0
    for i in range(n):
        if list_p[i] > i + 1:
            cnt += 1
            flg_jud = 1
        if list_p[i] == i + 1 and flg_jud == 0:
            cnt += 1
    print(cnt)

