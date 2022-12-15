from sys import stdin
readline = stdin.readline
a,b = map(int,readline().split())
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
