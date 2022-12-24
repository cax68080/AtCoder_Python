from sys import stdin
readline = stdin.readline
list_s = list(str(readline().rstrip('\n')))
#print(list_s)
count_calc = 0
count_0 = 0
for i in list_s:
    if int(i) > 0:
        if count_0 == 0:
            count_calc += 1
        else:
            count_calc += 2
            count_0 = 0
    else:
        if count_0 == 0:
            count_0 = 1
        else:
            count_calc += 1
            count_0 = 0
if count_0 == 1:
    count_calc += 1

print(count_calc)
