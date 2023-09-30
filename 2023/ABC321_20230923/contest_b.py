from sys import stdin
readline = stdin.readline
n,x = map(int,readline().rstrip("\n").split())
a_list = list(map(int,readline().rstrip("\n").split()))
a_list_sum = []
#print(a_list)
#print(sum(a_list))
#flg_end = 0
for i in range(0,101):
    a_list_sum = a_list.copy()
    a_list_sum.append(i)
    #print(a_list_sum)
    #print(sum(a_list_sum) - min(a_list_sum) - max(a_list_sum))
    if (sum(a_list_sum) - min(a_list_sum) - max(a_list_sum) ) >= x:
        print(i)
        #flg_end = 1
        exit()
    else:
        a_list_sum =[]
#if flg_end == 0:
print(-1)
