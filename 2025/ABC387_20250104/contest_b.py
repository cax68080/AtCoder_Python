from sys import stdin
readline = stdin.readline
grid = [[i * j for j in range(1, 10)] for i in range(1, 10)]
x = int(readline().rstrip("\n"))
result = 0
for i in range(9):
    for j in range(9):
        if grid[i][j] != x:
            result += grid[i][j]
print(result)