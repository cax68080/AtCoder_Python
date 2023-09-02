from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
s = readline().rstrip("\n")
result = ""
for i in range(n):
    result = result + s[i] * 2
print(result)
