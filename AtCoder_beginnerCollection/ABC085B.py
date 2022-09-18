n = int(input())
d = []
s = 0
k = 0
dan = 0
for i in range(n):
    d.append(int(input()))
d.sort(key=None,reverse=True)
for i in range(n):
    if i == 0:
        s = d[i]
        dan += 1
    else:
        k = d[i]
        if s > k:
            dan += 1
            s = k
print(dan)
