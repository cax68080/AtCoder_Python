from sys import stdin
readline = stdin.readline
n,d = map(int,readline().rstrip("\n").split())
list_s = []
list_a = []
flg_o = True
cnt = 0
cnt_max = 0
for _ in range(n):
    list_a = list(readline().rstrip("\n"))
    list_s.append(list_a)
    list_a = []
for i in range(d):
    for j in range(n):
        if list_s[j][i] == "x":
            flg_o = False
            break
    if flg_o:
        cnt += 1
    else:
        if cnt_max < cnt:
            cnt_max = cnt
        cnt = 0
        flg_o = True
if cnt_max < cnt:
    cnt_max = cnt

print(cnt_max)


