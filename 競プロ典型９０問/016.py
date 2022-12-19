from sys import stdin
readline = stdin.readline
n = int(readline())
coin_list = list(map(int,readline().split()))
coin_list.sort(key=None,reverse=True)
count = (n // coin_list[0]) + 1
coin_1 = 0
coin_2 = 0
coin_3 = 0
amari = 0
#print(count)
for i in range(count,0,-1):
   #print(i)
    coin_1 = i
    amari = n % (coin_list[0] * coin_1)
    print(amari)
    if amari == 0:
        coin_2 = 0
        pass
    else:
        coin_2 = amari // coin_list[1]
        if coin_2 == 0:
            pass
        else:
            amari = amari % (coin_list[1] * coin_2)
    print(amari)
    if amari == 0:
        coin_3 = 0
        pass
    else:
        coin_3 = amari // coin_list[2]
        if coin_3 == 0:
            pass
        else:
            amari = amari % (coin_list[2] * coin_3)
    print(amari)
    if amari == 0:
        print(coin_1 + coin_2 + coin_3)
        break
        
        