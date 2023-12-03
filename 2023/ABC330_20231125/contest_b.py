from sys import stdin
readline = stdin.readline
n,l,r = map(int,readline().rstrip("\n").split())
a_list = list(map(int,readline().rstrip("\n").split()))
result_list = []
x = 0
for i in a_list:
    if i < l:
        result_list.append(str(l))
    elif l <= i < r:
        result_list.append(str(i))
    else:
        result_list.append(str(r))
 
#print(result_list)
print(" ".join(result_list))

