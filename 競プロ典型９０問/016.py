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
# 金額×枚数を設定する変数
a_total = 0
b_total = 0
c_total = 0
total_cnt = 10 ** 18
# コイン枚数の上限9999枚まで処理を実行する
for a_cnt in range(10000):
    a_total = coin_a * a_cnt
    if n < a_total:
        break
    for b_cnt in range(10000 - a_cnt):
        b_total = coin_b * b_cnt
        if n < a_total + b_total:
            break
        else:
            sn = n - (a_total + b_total)
            if sn % coin_c == 0:
                c_cnt = sn / coin_c
                total_cnt = min(total_cnt,a_cnt + b_cnt + c_cnt)
print(int(total_cnt))        
