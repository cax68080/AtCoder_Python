from sys import stdin
readline = stdin.readline
x,y = map(int,readline().rstrip("\n").split())
if x > y:
    print(0)
else:
    s = y - x
    a = s // 10
    if s % 10 == 0:
        print(a)
    else:
        print(a + 1)
    