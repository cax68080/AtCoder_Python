from sys import stdin
readline = stdin.readline
n = int(readline())
list_a = list(map(int,readline().split()))
list_a.insert(0,0)
#print(list_a)
q = int(readline())
for i in range(q):
    list_query = list(map(int,readline().split()))
    if list_query[0] == 1:
        #list_a.pop([list_query[1]])
        list_a[list_query[1]] = list_query[2]
    else:
        print(list_a[list_query[1]])
