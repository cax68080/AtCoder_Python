from sys import stdin
readline = stdin.readline
n = int(readline())
n = 2 * n + 1
num_list = [0 for i in range(n + 1)]
num_list[0] = 1
while True:
    if num_list.count(0) > 0:
        ans = num_list.index(0)
        num_list[ans] = 1
    else:
        ans = 0
        break
    print(ans,flush=True)
    ins = int(readline())
    if ins == 0:
        #print(ins)
        break
    elif num_list[ins] == 0:
        #print(ins)
        num_list[ins] = 1
    else:
        break
    #print(num_list)

