from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_p = list(map(int,readline().rstrip("\n").split()))
#print(list_p)
q = int(readline().rstrip("\n"))
#print(q)
pos_a = 0
pos_b = 0 
for _ in range(q):
    a,b = map(int,readline().rstrip("\n").split())
    #print(a)
    #print(b)
    pos_a = list_p.index(a)
    pos_b = list_p.index(b)
    #print(pos_a)
    #print(pos_b)
    if pos_a < pos_b:
        print(a)
    else:
        print(b)
