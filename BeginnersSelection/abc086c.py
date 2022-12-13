from sys import stdin
readline = stdin.readline
n = int(readline())
t_old = 0
x_old = 0
y_old = 0
flag = True
for _ in range(n):
    t,x,y = map(int,readline().split())
    distanse = abs((x - x_old) + (y - y_old))
    time = t- t_old
    t_old  = t
    x_old = x
    y_old = y
    if time < distanse:
        flag = False
        break
    if time % 2 != distanse % 2:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")