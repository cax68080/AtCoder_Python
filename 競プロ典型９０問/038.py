from sys import stdin
readline = stdin.readline
LARGE = 10 ** 18
a,b = map(int,readline().split())
def get_gcd(a,b):
    r = 0
    if a >= b:
        x = a
        y = b
    else:
        x = b
        y = a
    flg = True
    while flg:
        r = x % y
        if r == 0:
            return y
            break
        else:
            x = y
            y = r

gcd = get_gcd(a,b)
#print(gcd)
lcm = a * b // gcd
if lcm > LARGE:
    print("Large")
else:
    print(lcm)
        