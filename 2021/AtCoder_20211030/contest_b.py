from sys import stdin
readline = stdin.readline
n = int(readline())
tree_list = [0 for _ in range(n)]
result = ""
#print(tree_list[3][4])
for i in range(n - 1):
    a,b = map(int,readline().split())
    a = a - 1
    b = b - 1
    tree_list[a] += 1
    tree_list[b] += 1
if tree_list.count(n - 1) > 0:
    print("Yes")
else:
    print("No")
    