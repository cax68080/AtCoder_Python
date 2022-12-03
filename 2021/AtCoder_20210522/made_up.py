n = input()
n = int(n)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
b2 = []
s = 0
for i in range(n):
    #t = 0
    #t = int(c[i]) -1 
    b2.append(b[int(c[i]) -1])
for j in range(n):
    s += b2.count(a[j])  
print(s)

