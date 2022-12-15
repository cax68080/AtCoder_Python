from sys import stdin
readline = stdin.readline
n = int(readline())
list_p = list(map(int,readline().split()))
list_q = list(map(int,readline().split()))
ix = 0
cnt = 0
for i in list_p:
    for j in range(ix,len(list_q)):
        print(i)
        print(list_q[j])
        if list_q[j] % i == 0:
            ix = j
            cnt += 1
            break
print(cnt)