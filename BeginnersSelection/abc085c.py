from sys import stdin
readline = stdin.readline
# a:10000円札の枚数
# b:5000円札の枚数
# c:1000円札の枚数
# a + b + c = n
# 10000a + 5000b + 1000c = y
# 9a + 4b = (y - 1000n) / 1000
n,y = map(int,readline().split())
# 10000円札がn枚の金額がy円より少ない場合は対象外
# 1000円札がn枚の金額がy円より多い場合は対象外
if (y > 10000 * n) or (y < 1000 * n):
    print(-1," ",-1," ",-1)
else:
    end_flg = 0
    for a in range(n + 1):
        if end_flg == 0:
            for b in range(n + 1):
                c = n - (a + b)
                if c >= 0:
                    price = 10000 * a + 5000 * b + 1000 * c
                    if price == y:
                        end_flg = 1
                        print(a," ",b," ",c)
                        break
                    else:
                        price = 0
                else:
                    break 
        else:
            break
    if end_flg == 0:
         print(-1," ",-1," ",-1)
         