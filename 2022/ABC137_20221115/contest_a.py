from sys import stdin
readline = stdin.readline
a,b = map(int,readline().split())
plus = a + b
minus = a - b
kakeru = a * b
print(max([plus,minus,kakeru])) 