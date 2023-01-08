from sys import stdin
readline = stdin.readline
n = int(readline())
result_list = []
rev_n = n * -1
for _ in range(n):
    s = readline().rstrip("\n")
    result_list.insert(0,s)
for i in result_list:
    print(i)    
