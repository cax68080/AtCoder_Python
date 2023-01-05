from sys import stdin
readline = stdin.readline
n,q = map(int,readline().split())
list_a = list(map(int,readline().split()))
#list_a.insert(0,0)
pos = 0
#print(list_a)
for i in range(q):
    t1,t2,t3 = map(int,readline().split())
    t2 = t2 - pos
    t3 = t3 - pos
    if t1 == 1:
        ta = list_a[t2 - 1]
        tb = list_a[t3 - 1]
        list_a[t2 - 1] = tb
        list_a[t3 - 1] = ta
    elif t1 == 2:
        pos += 1
        if pos >= n:
            pos = 0
    elif t1 == 3:
        #print(t2 - 1)
        #print(list_a)
        print(list_a[t2 - 1])
    else:
        pass
