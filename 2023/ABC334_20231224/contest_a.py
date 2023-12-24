from sys import stdin
readline = stdin.readline
b,g = map(int,readline().rstrip("\n").split())
if b > g:
    print("Bat")
else:
    print("Glove")
    