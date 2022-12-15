from sys import stdin
readline = stdin.readline
n,q = map(int,readline().split())
list_a = list(range(1,n + 1))
for i in range(q):
    x = int(readline().rstrip('\n'))
    pos = list_a.index(x)
    #print(pos)
    num = list_a.pop(pos)
    if pos != n - 1:
        list_a.insert(pos,num)
    else:
        list_a.insert(pos - 1,num)  
print(*list_a)