from sys import stdin
readline = stdin.readline
s_list = list(str(readline().rstrip("\n")))
result_list = []
for i in s_list:
    result_list.append(i)
    if len(result_list) >= 3:
        if result_list[-1] == "C" and result_list[-2] == "B" and result_list[-3] == "A":
            for _ in range(3):
                result_list.pop(-1)
    #print(result_list)        
print("".join(result_list))