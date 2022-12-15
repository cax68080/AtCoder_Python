from sys import stdin
readline = stdin.readline
def fab(n,m):
    list_a = [0 for i in range(n)]
    for i in range(m):
        a1,a2 = map(int,readline().split())
        list_a[a1-1] += 1
        list_a[a2-1] += 1
    return list_a

n,m = map(int,readline().split())
if n == 0 or m == 0:
    print("Yes")
else:
    toy_a = fab(n,m)
    toy_b = fab(n,m)
    toy_a.sort(key=None,reverse=True)
    toy_b.sort(key=None,reverse=True)
    result = "Yes"
    for i in range(len(toy_a)):
        if toy_a[i] == toy_b[i]:
            continue
        else:
            result = "No"
            break
    print(result)
