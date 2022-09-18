from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
list_a = list(map(int,readline().split()))
list_b = list(map(int,readline().split()))
list_c = []
result = "Yes"
for i in range(m):
    mm = list_b[i]
    if list_a.count(mm) == 0:
        result = "No"
        break
    elif list_a.count(mm) == 1:
        p = list_a.index(mm)
        if list_c.count(p) > 0:
            result = "No"
            break
        else:
            list_c.append(p)
    else:
        #p = list_a.index(mm)
        chk = "NG"
        for j in range(n):
            if list_a[j] == mm:
                if list_c.count(j) == 0:
                    list_c.append(j)
                    chk = "OK"
                    break
        if chk == "NG":
            result = "No"
            break
    #print(list_c)
print(result)