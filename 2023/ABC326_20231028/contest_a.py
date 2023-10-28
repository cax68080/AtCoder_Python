from sys import stdin
readline = stdin.readline
x,y = map(int,readline().rstrip("\n").split())
if x > y:
    if x - y <= 3:
        print("Yes")
    else:
        print("No")
else:
    if y - x <= 2:
        print("Yes")
    else:
        print("No")
