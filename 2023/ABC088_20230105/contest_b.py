from sys import stdin
readline = stdin.readline
n = int(readline())
list_card = list(map(int,readline().split()))
list_card.sort(key=None,reverse=True)
alice_point = 0
bob_point = 0
seq = 1
for i in list_card:
    if seq % 2 != 0:
        alice_point += i
    else:
        bob_point += i
    seq += 1
print(alice_point - bob_point)