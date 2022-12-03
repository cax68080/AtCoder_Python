from sys import stdin
readline = stdin.readline

n,a,b = map(int,readline().split())

def set_column(num):
    str_num = str(num)
    if len(str_num) == 1:
        str_num = "000" + str_num
    elif len(str_num) == 2:
        str_num = "00" + str_num
    elif len(str_num) == 3:
        str_num = "0" + str_num
    else:
        str_num = str_num
    return str_num

result = 0

for i in range(1,n + 1):
    str_num = set_column(i)
    col_total = int(str_num[0]) + int(str_num[1]) + int(str_num[2]) + int(str_num[3])
    if a <= col_total <= b:
        result += i
print(result)
