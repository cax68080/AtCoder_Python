from sys import stdin
readline = stdin.readline
#def fab():
n = int(readline())
s_list = []
cnt_list = [0 for i in range(n)]
for i in range(n):
    s = str(readline())
    if s_list.count(s) == 0:
        s_list.append(s)
    j = s_list.index(s)
    cnt_list[j] += 1
k = cnt_list.index(max(cnt_list))
result = s_list[k]
print(result)
    

