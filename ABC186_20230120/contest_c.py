from sys import stdin
readline = stdin.readline
n = int(readline())
def chg_oct(num):
    ans = 0
    amr = 0
    result = ""
    while True:
        ans = num // 8
        amr = num % 8
        if ans == 0:
            result = result + str(amr)
            break
        else:
            result = result + str(ans)
            num = amr
    return result
count = 0
num_10 = ""
num_8 = ""
for i in range(1,n + 1):
    num_10 = str(i)
    num_8 = chg_oct(i)
    #print(num_8)
    if ("7" in num_10) or ("7" in num_8):
        print(num_10)
        pass
    else:
        #print(num_8)
        count += 1
print(count)