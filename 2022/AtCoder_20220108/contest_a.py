from sys import stdin
readline = stdin.readline
def fab(t):
    result = t ** 2 + 2 * t +3
    return result
t = int(readline())
answer = fab(fab(fab(t) + t) + fab(fab(t)))
print(answer)