from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
list_line = []
list_col = [0] * w
list_result = [[0 for i in range(w)] for j in range(h)]
list_matrix = []
list_a = []
sum_list = []
for _ in range(h):
    list_a = list(map(int,readline().split()))
    list_line.append(sum(list_a))
    list_matrix.append(list_a)
    for i in range(w):
        list_col[i] += list_a[i]
for i in range(h):
    for j in range(w):
        list_result[i][j] = list_line[i] + list_col[j] - list_matrix[i][j] 
for k in list_result:
    print(*k)        
        
        
