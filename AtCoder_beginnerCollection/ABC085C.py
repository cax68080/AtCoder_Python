from sys import stdin
readline = stdin.readline
def fab(bill,n,y):
    max_10000 = 0
    max_5000 = 0
    cnt_10000 = 0
    cnt_5000 = 0
    cnt_1000 = 0
    max_10000 = y // bill[0]
    for i in range(max_10000):
        price = y - bill[0] * i
        

bill = [10000,5000,1000]
cnt_list = []
n,y = map(int,readline().split())
fab(bill,n,y)
