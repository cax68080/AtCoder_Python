from sys import stdin
readline = stdin.readline
q = int(readline())
x_list=[]
for _ in range(q):
    t,x = map(int,readline().split())
    if t == 1:
        x_list.insert(0,x)
    elif t == 2:
        x_list.append(x)
    else:
        print(x_list[x - 1])
