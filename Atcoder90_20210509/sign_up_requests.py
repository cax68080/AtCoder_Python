import sys
input = sys.stdin.readline
n = int(input())
s = [None]*n
d = 1
t = ""
i = 0
for i in s:
    t = input()
    if s.count(t) == 0:
        print(d)
        s.append(t)
    d += 1


