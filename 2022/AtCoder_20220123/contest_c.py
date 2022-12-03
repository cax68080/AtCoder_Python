from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
s_list = list(map(str,readline().split()))
t_list = set(map(str,readline().split()))
cnt = 0
for i in s_list:
    if i in t_list:
        print("Yes")
    else:
        print("No")
    
