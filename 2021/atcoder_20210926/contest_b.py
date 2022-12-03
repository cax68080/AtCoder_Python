from sys import stdin
readline = stdin.readline
def fab(a,b,c):
    s = 0
    bt = 0
    ct = 0
    for i in b:
        bt += int(i) * a**s
        s += 1
    s = 0
    for j in c:
        ct += int(j) * a**s
        s += 1 
    #print(bt)
    #print(ct)
    return bt * ct

a = int(readline())
b,c = map(str,readline().split())
blist = list(b)
blist.reverse()
clist = list(c)
clist.reverse()
print(fab(a,blist,clist))
