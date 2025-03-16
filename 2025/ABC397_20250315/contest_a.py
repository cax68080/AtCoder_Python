from sys import stdin
readline = stdin.readline
x = float(readline().rstrip())
if x >= 38.0:
    print("1")
elif 37.5 <= x < 38.0:
    print("2")
elif x < 37.5:
    print("3")