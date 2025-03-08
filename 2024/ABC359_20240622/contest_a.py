from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
count = 0
s = ""
for _ in range(n):
    s = str(readline().rstrip("\n"))
    if s == "Takahashi":
        count += 1
print(count)