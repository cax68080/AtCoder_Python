l,m,n = map(int,input().split())
def get_gcd(a,b):
    i = False
    x = 0
    y = 0
    if int(a) > int(b):
        x = a
        y = b
    else:
        x = b
        y = a
    while i == False:
        r = x % y
        if r != 0:
            x = y
            y = r
        else:
            i = True
    return(y)
ga = 0
gb = 0
gc = 0
ga = get_gcd(l,m)
gb = get_gcd(ga,n)
gc = (int(l // gb) - 1) + (int(m // gb) - 1) + (int(n // gb)  - 1)
print(gc) 
