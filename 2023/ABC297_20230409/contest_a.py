from sys import stdin
readline = stdin.readline
n,d = map(int,readline().split())
l_time = list(map(int,readline().split()))
#print(l_time)
click_time = 0
for i in range(len(l_time) - 1):
    if l_time[i + 1] - l_time[i] <= d:
        click_time = l_time[i + 1]
        break
if click_time == 0:
    print(-1)
else:
    print(click_time)
