from sys import stdin
readline = stdin.readline
def fab(w,list_cheese):
    taste = 0
    for i in range(len(list_cheese)):
        if list_cheese[i][1] < w:
            taste += list_cheese[i][0] * list_cheese[i][1]
            w -= list_cheese[i][1]
        else:
            taste += list_cheese[i][0] * w
            break
    return taste

n,w = map(int,readline().split())
list_cheese = []
for i in range(n):
    list_c = list(map(int,readline().split()))
    list_cheese.append(list_c)
list_cheese.sort(key=lambda x:x[0],reverse=True)
print(fab(w,list_cheese))
#print(list_cheese)