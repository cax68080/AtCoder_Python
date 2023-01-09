from sys import stdin
readline = stdin.readline
n,k = map(int,readline().split())
list_tree = []
for _ in range(n):
    list_tree.append(int(readline()))
list_tree.sort(key=None,reverse=True)
result = max(list_tree) - min(list_tree)
diff = 0
for i in range(len(list_tree)):
    if i + k > len(list_tree):
        break
    else:
        #print(list_tree[i])
        #print(list_tree[i + k - 1])
        diff = list_tree[i] - list_tree[i + k -1]
        if result > diff:
            result = diff
        else:
            pass
print(result)         