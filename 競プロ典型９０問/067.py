from sys import stdin
readline = stdin.readline
def _8_to_10(x):
    list_a = list(str(x))
    num = len(list_a) - 1
    result = 0
    for i in list_a:
        result += (int(i) * (8 ** num))
        num -= 1
    return result
def _10_to_9(x):
    str_number = ""
    flg = True
    ans = 0
    ans_old = x
    ama = 0
    while flg == True:
        ans = ans_old // 9
        if ans > 0:
            ama = ans_old % 9
            str_number = str(ama) + str_number
            ans_old = ans
        else:
            str_number = str(ans_old) + str_number
            flg = False
    
    str_number = str_number.replace("8","5")
    return int(str_number)

n,k = map(int,readline().split())
for _ in range(k):
    n = _8_to_10(n)
    #print(n)
    n = _10_to_9(n)
    #print(n)
print(n)

            
            
        
    