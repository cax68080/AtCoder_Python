from sys import stdin
readline = stdin.readline

# 金額を取得する
n = int(readline())

# コインの金額を取得、金額の高い順にソートする
coin_list = list(map(int,readline().split()))
coin_list.sort(key=None,reverse=True)

# 金額が高い順に変数に設定
coin_a = coin_list[0]
coin_b = coin_list[1]
coin_c = coin_list[2]

# コインの枚数を計上する変数
a_cnt = 0
b_cnt = 0
c_cnt = 0
# 金額の余りを設定する変数
a_amari = 0
b_amari = 0
c_amari = 0
# 金額×枚数を設定する変数
a_total = 0
b_total = 0
c_total = 0
total_cnt = 0
# コイン枚数の上限9999枚まで処理を実行する
for a_cnt in range(10000):
    a_total = coin_a * a_cnt
    if n < a_total:
        a_cnt -= 1
        break
    else:
        a_amari = n - a_total
    for b_cnt in range(10000 - a_cnt):
        b_total = coin_b * b_cnt
        if a_amari < b_total:
            b_cnt -= 1
            break
        else:
            b_amari = a_amari - b_total
            if b_amari == 0:
                #c_cnt = 0
                break
            else:
                c_amari = b_amari % coin_c
                if c_amari == 0:
                    c_cnt = b_amari / coin_c
                    if (total_cnt > 0) and  (total_cnt > a_cnt + b_cnt + c_cnt):
                        #print(a_cnt)
                        #print(b_cnt)
                        #print(c_cnt)
                        total_cnt = a_cnt + b_cnt + c_cnt
                    elif total_cnt == 0:
                        #print(a_cnt)
                        #print(b_cnt)
                        #print(c_cnt)
                        total_cnt = a_cnt + b_cnt + c_cnt
                    else:
                        pass
                    #break
                else:
                    pass

print(int(total_cnt))        
