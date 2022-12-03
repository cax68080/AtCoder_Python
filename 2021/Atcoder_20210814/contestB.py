from sys import stdin
readline = stdin.readline
def fab(s,t):
    result = 0
    for a in range(s + 1):
        for b in range(s + 1 - a):
            for c in range(s + 1 - a -b):
                if a * b * c <= t:
                    result += 1
    return result
s,t = map(int,readline().split())
print(fab(s,t))