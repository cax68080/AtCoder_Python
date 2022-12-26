from sys import stdin
readline = stdin.readline
n = int(readline())
s_list = list(readline().rstrip('\n'))
num_list = []
def num_count(n):
    return (n * (n + 1)) // 2
all_count = num_count(n)
count_s = 0
count_t = 0
ox_flag = ""
for i in s_list:
    if ox_flag == "":
        ox_flag = i
        count_s = 1
    elif ox_flag == i:
        count_s += 1
    else:
        ox_flag = i
        num_list.append(count_s)
        count_s = 1
num_list.append(count_s)
#print(num_list)
for j in num_list:
    count_t += num_count(j)
print(all_count - count_t)
