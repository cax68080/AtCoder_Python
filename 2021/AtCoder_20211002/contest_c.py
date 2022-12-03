from sys import stdin
readline = stdin.readline
def fab(n):
    n_list = list(n.rstrip('\n'))
    n_list.sort(key=None,reverse=True)
    a = ""
    b = ""
    cnt = 0
    #print(n_list)
    if len(n_list) % 2 == 0:
        flg = 0
    else:
        flg = 1
    for i in n_list:
        cnt += 1
        if flg == 1 and cnt == len(n_list):
            b = b + i
            break
        if cnt % 2 != 0:
            a = a + i 
        else:
            b = b + i 
    #print(a)
    #print(b)
    result = int(a) * int(b)
    return result

n = str(readline())
print(fab(n))