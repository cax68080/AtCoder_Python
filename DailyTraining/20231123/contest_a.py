from sys import stdin
readline = stdin.readline
list_s = list(str(readline().rstrip("\n")))
result_list = ["0"]
for i in range(3):
    result_list.append(str(list_s[i]))
print("".join(result_list))