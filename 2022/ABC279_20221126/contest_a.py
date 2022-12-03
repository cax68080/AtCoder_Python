from sys import stdin
readline = stdin.readline
s = list(str(readline().rstrip('\n')))
count = 0
count = s.count('v') + s.count('w') * 2
print(count)