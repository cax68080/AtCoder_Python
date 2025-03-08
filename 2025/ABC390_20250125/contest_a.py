from sys import stdin
readline = stdin.readline
list_a = list(map(int, readline().rstrip("\n").split()))
seikai_list = [1, 2, 3, 4, 5]
dummy_num = 0
chg_flg = False
#print(list_a)
if list_a[0] == 1:
    pass
else:
    dummy_num = list_a[0]
    list_a[0] = list_a[1]
    list_a[1] = dummy_num
    chg_flg = True
if list_a[1] == 2:
    pass
elif chg_flg == False:
    if list_a[0] == 2:
        dummy_num = list_a[1]
        list_a[1] = list_a[0]
        list_a[0] = dummy_num
        chg_flg = True
elif list_a[2] == 2:
        dummy_num = list_a[1]
        list_a[1] = list_a[2]
        list_a[2] = dummy_num
        chg_flg = True
else:
     pass
if list_a[2] == 3:
        pass
elif chg_flg == False:
    if list_a[1] == 3:
        dummy_num = list_a[2]
        list_a[2] = list_a[1]
        list_a[1] = dummy_num
        chg_flg = True
    elif list_a[3] == 3:
        dummy_num = list_a[3]
        list_a[3] = list_a[2]
        list_a[2] = dummy_num
        chg_flg = True
if list_a[3] == 4:
        pass
elif chg_flg == False:
    if list_a[2] == 4:
        dummy_num = list_a[3]
        list_a[3] = list_a[2]
        list_a[2] = dummy_num
        chg_flg = True
    elif list_a[4] == 4:
        dummy_num = list_a[3]
        list_a[3] = list_a[4]
        list_a[4] = dummy_num
        chg_flg = True
if list_a[4] == 5:
        pass
elif chg_flg == False:
    if list_a[3] == 5:
        dummy_num = list_a[4]
        list_a[4] = list_a[3]
        list_a[3] = dummy_num
        chg_flg = True
    else:
        pass
#print(list_a)
if chg_flg == True:
    if list_a == seikai_list:
        print("Yes")
    else:
        print("No")
else:
    print("No")