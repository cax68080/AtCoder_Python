from sys import stdin
readline = stdin.readline
n = int(readline())
list_a = list(map(int,readline().split()))
#print(list_a)
q = int(readline())
for _ in range(q):
    b = int(readline())
    min_b = b
    for i in list_a:
        abs_b = abs(i - b)
        #print(b)
        if abs_b < min_b:
            min_b = abs_b
    print(min_b)



