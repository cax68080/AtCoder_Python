from sys import stdin
readline = stdin.readline
def data_chk(num,cnt):
    end_flg = "1" * cnt
    parm = "0" + str(cnt) + "b"
    str_bin = format(num,parm)
    list_bin = list(str_bin)
    if str_bin == end_flg:
        result = "END"
    else:
        result = ""
        if list_bin.count("0") == list_bin.count("1"):
            pass
        else:
            result = "NG"
        cnt_0 = 0
        cnt_1 = 0
        for i in list_bin:
            if result == "NG":
                break
            if i == "0":
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_1 > cnt_0:
                result = "NG"
                break
        if result == "NG":
            pass
        else:
            str_bin = str_bin.replace("0","(")
            str_bin = str_bin.replace("1",")")
            result = str_bin
    
    return result
        
    
binary_data = 0b0
n = int(readline())
if n % 2 == 0:
    flg = True
else:
    flg = False

while flg:
    binary_data += 0b1
    result = data_chk(binary_data,n)
        
    if result == "END":
        flg = False
    elif result == "NG":
        pass
    else:
        print(result)