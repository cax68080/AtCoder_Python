s = int(input())
t = list(map(int,input().split()))
l = []
c = 0
endflg = False
while endflg == False:
    for i in range(s):
        if t[i] % 2 == 0:
            k = t[i]/2
            l.insert(i,k)
        else:
            endflg = True
            break
    if endflg == False:
        t.clear()
        t.extend(l)
        l.clear
        c += 1
print(c)




