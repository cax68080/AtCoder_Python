import timeit
import cProfile
from sys import stdin
def distance():
    readline = stdin.readline
    n = int(readline())
    a = []*2
    b = []*n
    c = []*n
    for i in range(n):
        a = list(map(int,readline().split()))
        b.append(a)
    for j in range(n-1):
        for k in range(j+1,n):
            l = 0
            l = max(abs(b[j][0]-b[k][0]),abs(b[j][1]-b[k][1]))
            c.append(l)
    c.sort(key=None,reverse=True)
    return c[1]
#print(distance())
cProfile.run('distance()')
#result = timeit.timeit('distance()', globals=globals(), number=1)
#print(result)



