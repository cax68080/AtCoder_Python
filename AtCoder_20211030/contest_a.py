from sys import stdin
readline = stdin.readline
def fab(s):
    t_list = []
    s_list = list(s)
    t = s_list[0] + s_list[1] + s_list[2]
    t_list.append(t)
    t = s_list[0] + s_list[2] + s_list[1]
    t_list.append(t)
    t = s_list[1] + s_list[0] + s_list[2]
    t_list.append(t)
    t = s_list[1] + s_list[2] + s_list[0]
    t_list.append(t)
    t = s_list[2] + s_list[0] + s_list[1]
    t_list.append(t)
    t = s_list[2] + s_list[1] + s_list[0]
    t_list.append(t)
    t_list.sort(key=None,reverse=False)
    cnt = 0
    st = ""
    for i in range(len(t_list)):
        if st != t_list[i]:
            st = t_list[i]
            cnt += 1
    return cnt
s = str(readline())
print(fab(s))