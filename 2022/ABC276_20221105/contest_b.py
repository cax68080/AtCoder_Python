from sys import stdin
readline = stdin.readline

n,m = map(int,readline().split())
city_list = [[]  for _ in range(n)]
for i in range(m):
    a,b = map(int,readline().split())
    city_list[a - 1].append(b)
    city_list[b - 1].append(a)
for (i,v) in enumerate(city_list):
    #result = str(len(city_list[i])) + " "
    #print(v)
    v.sort()
    #for j in city_list[i]:
        #result = result + str(j) + " "
    print(len(v),*v)    

