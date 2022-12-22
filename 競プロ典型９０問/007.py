from sys import stdin
readline = stdin.readline
n = int(readline())

list_a = list(map(int,readline().split()))

list_a.sort(key=None,reverse=False)

#pos_s = 0
#pos_e = n - 1
#chk_point = 0

q = int(readline())

for _ in range(q):
    b = int(readline())
    pos_s = 0
    pos_e = n - 1
    chk_point = 0
    while (pos_e - pos_s) > 1:
        chk_point = (pos_e + pos_s) // 2
        if list_a[chk_point] >= b:
            pos_e = chk_point
        else:
            pos_s = chk_point
        #print(pos_s)
        #print(pos_e)
    min_a = abs(b - list_a[pos_s])
    max_a = abs(b - list_a[pos_e])
    #print(min_a)
    #print(max_a)
    if min_a <= max_a:
        print(min_a)
    else:
        print(max_a)
    
>>>>>>> origin/main

