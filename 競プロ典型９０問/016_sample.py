N = int(input())
A, B, C = map(int,input().split())

ans = pow(10, 18)
for a in range(10000):
    if A*a > N:
        break
    for b in range(10000-a):
        s = A*a + B*b
        if s > N:
            break
        sn = N - s    
        if sn % C == 0:
            c = sn / C
            ans = min(ans, a+b+c)

print(int(ans))