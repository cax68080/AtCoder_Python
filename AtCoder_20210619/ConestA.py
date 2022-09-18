from sys import stdin
import math
readline = stdin.readline
def fab(n):
    x = math.floor(int(n) * 1.08)
    if x < 206:
        return "Yay!"
    elif x > 206:
        return ":("
    else:
        return "so-so"
a = int(readline())
print(fab(a))

