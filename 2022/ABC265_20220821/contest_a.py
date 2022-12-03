from sys import stdin
readline = stdin.readline
a = 0
b = 0
x,y,n = map(int,readline().split())
a = n // 3
b = n % 3
if y < x * 3:
    print(y * a + x * b)
elif y >= x * 3:
    print(x *n)
