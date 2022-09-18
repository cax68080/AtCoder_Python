a,b = map(int,input().split())
s = (a * b) % 2
if s == 0:
    print('Even')
else:
    print('Odd')
