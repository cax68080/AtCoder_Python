from sys import stdin
readline = stdin.readline
n = 1048576
q = int(readline())
n_list = [-1 for i in range(n)]
for i in range(q):
    t,x = map(int,readline().split())
    if t == 1:
        h = x
        i = h % n
        while True:
            if n_list[i] != -1:
                h += 1
                i = h % n
            else:
                n_list[i] = x
                break 
    elif t == 2:
        i = x % n
        print(n_list[i])
    else:
        continue


            

