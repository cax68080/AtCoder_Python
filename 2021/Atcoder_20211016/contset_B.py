from sys import stdin
readline = stdin.readline
def fab(r,g,b):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt = 0
    r_mod3 = r % 3
    g_mod3 = g % 3
    b_mod3 = b % 3
    if r_mod3 == g_mod3:
        if r > g:
            cnt1 = r 
        else:
            cnt1 = g
        if cnt1 > 0:
            cnt = cnt1
    if r_mod3 == b_mod3:
        if r > b:
            cnt2 = r
        else:
            cnt2 = b
        if cnt == 0:
            cnt = cnt2
        if cnt2 > 0 and cnt > 0 and cnt > cnt2:
            cnt = cnt2
    if b_mod3 == g_mod3:
        if b > g:
            cnt3 = b
        else:
            cnt3 = g
        if cnt == 0:
            cnt = cnt3
        if cnt3 > 0 and cnt > 0  and cnt > cnt3:
            cnt = cnt3
    if cnt == 0:
        return -1
    else:
        return cnt
t = int(readline())
for i in range(t):
    r,g,b = map(int,readline().split())
    print(fab(r,g,b))