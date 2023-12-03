from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
a_list = list(map(int,readline().rstrip("\n").split()))
a_list_sort = sorted(a_list,reverse=True)
#print(a_list_sort)
result_list = []
pos = 0
for i in a_list:
    pos = a_list_sort.index(i)
    result_list.append(str(sum(a_list_sort[:pos])))
print(" ".join(result_list))
