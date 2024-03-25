from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_a = list(map(int,readline().rstrip("\n").split()))
list_hit = []
list_lost = []
count_hit = 0
count_lost = 0
for i in list_a:
    if i == 0:
        count_lost += 1
    else:
        count_hit += 1
    list_hit.append(count_hit)
    list_lost.append(count_lost)
#print(list_a)
#print(list_hit)
#print(list_lost)
hit = 0
lost = 0
q = int(readline().rstrip("\n"))
for _ in range(q):
    l,r = map(int,readline().rstrip("\n").split())
    if l == 1:
        hit = list_hit[r - 1]
        lost = list_lost[r - 1]
    else:
        hit = list_hit[r - 1] - list_hit[l - 2]
        lost = list_lost[r - 1] - list_lost[l - 2]
    #print(hit)
    #print(lost)
    if hit == lost:
        print("draw")
    elif hit > lost:
        print("win")
    elif hit < lost:
        print("lose")
    else:
        pass


