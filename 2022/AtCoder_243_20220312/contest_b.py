from sys import stdin
readline = stdin.readline
def fab(n,a_list,b_list):
    cnt_pos = 0
    cnt_num = 0
    for i in range(n):
        if a_list[i] == b_list[i]:
            cnt_pos += 1
        elif a_list[i] in b_list:
            cnt_num += 1
        else:
            continue
    return(cnt_pos,cnt_num)
n = int(readline())
a_list = list(map(int,readline().split()))
b_list = list(map(int,readline().split()))
pos,num = fab(n,a_list,b_list)
print(pos)
print(num)