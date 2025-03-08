from sys import stdin
readline = stdin.readline
q = int(readline().rstrip("\n"))
list_l = []
result = 0
for _ in range(q):
    s = readline().rstrip("\n")
    if len(s) > 1:
        a, b = map(int, s.split())
    else:
        a = int(s)
    if a == 1:
        list_l.append(b)
    elif a == 2:
        list_l.pop(0)
    else:
        for i in range(b - 1):
            result += list_l[i] 
        print(result)
        result = 0