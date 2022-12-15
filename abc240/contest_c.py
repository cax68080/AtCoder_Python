from sys import stdin
readline = stdin.readline
n,x = map(int,readline().split())
list_a = []
list_b = []
list_c = []
for i in range(n):
    list_a = list(map(int,readline().split()))
    if len(list_b) == 0:
        list_b.extend(list_a)
        list_a.clear()
    else:
        #print(list_a)
        #print(list_b)
        for j in range(len(list_b)):
            for k in range(len(list_a)):
                c = list_b[j] + list_a[k]
                if c <= x:
                    list_c.append(c)
                #print(list_c)
        list_b.clear()
        list_b.extend(list_c)
        list_c.clear()
        #print(list_b)
if list_b.count(x) > 0:
    print("Yes")
else:
    print("No")
    
    
    