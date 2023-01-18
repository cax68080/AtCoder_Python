from sys import stdin
readline = stdin.readline
n = int(readline())
mount_list = []
sort_list = []
for _ in range(n):
    s,t = map(str,readline().split())
    mount_list.append(int(t))
    mount_list.append(s)
    sort_list.append(mount_list)
    mount_list = []
sort_list.sort(key=None,reverse=True)
print(sort_list[1][1])
    