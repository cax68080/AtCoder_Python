from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
j_list = []
result_list = []
result = ""
k = 0
for i in range(n+1):
    for j in range(1,10):
        if n % j ==0:
            k = n // j
            if i % k == 0:
                j_list.append(j)
    if len(j_list) > 0:
        result_list.append(j_list[0])
    else:
        result_list.append("-")
    j_list = []
    k = 0
for i in result_list:
    result = result + str(i)
print(result) 
        