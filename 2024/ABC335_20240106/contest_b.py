from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
x = 0
y = 0
z = 0
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z <= n:
                print(str(x) + " " + str(y) + " " + str(z))

