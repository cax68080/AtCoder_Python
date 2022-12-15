from sys import stdin
readline = stdin.readline
h,a = map(int,readline().split())
attack_count = h // a
if h % a == 0:
    print(attack_count)
else:
    print(attack_count + 1)
