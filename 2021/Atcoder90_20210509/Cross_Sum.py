import cProfile
from sys import stdin
readline = stdin.readline
def fab():
    h,w = map(int,readline().split())
    x = []
    a = []
    wt = []
    ht = []
    s = 0
    p = ""
    #標準入力で２次元配列xを作る
    #各行の合計リストwtを作る
    for i in range(h):
        a = list(map(int,readline().split()))
        wt.append(sum(a))
        x.append(a)
    #各列の合計リストhtを作る
    for j in range(w):
        for i in range(h):
            s += x[i][j]
        ht.append(s)
        s = 0
    #行列を集計してリストを出力する。
    for i in range(h):
        for j in range(w):
            s = wt[i] + ht[j] - x[i][j]
            p = p + str(s) + " "
        p = p + "\n"
    return p

#cProfile.run('fab()')
print(fab())


        
        
        

