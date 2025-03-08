from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
h_list = list(map(int,readline().rstrip("\n").split()))
building = h_list[0]
result = -1
for i in range(1,n,1):
    if h_list[i] > building:
        result = i + 1
        break
print(result)
