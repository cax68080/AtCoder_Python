from sys import stdin
readline = stdin.readline
n = int(readline())
a_list = list(map(int,readline().split()))
result = "No"
for i in range(len(a_list)):
    for j in range(i + 1,len(a_list)):
        for k in range(j + 1,len(a_list)):
            #print(i,j,k)
            if a_list[i] + a_list[j] + a_list[k] == 1000:
                result = "Yes"
                break
        if result == "Yes":
            break
    if result == "Yes":
        break
print(result)