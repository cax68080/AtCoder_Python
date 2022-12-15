from sys import stdin
import bisect
readline = stdin.readline
def fab(n,a_list,x):
    result = 0
    pos = bisect.bisect_left(a_list,x)
    #print(t_list)
    #print(str(x) + "," + str(pos) )
    result = n - pos
    return result
n,q = map(int,readline().split())
a_list = list(map(int,readline().split()))
a_list.sort(key=None,reverse=False)
for i in range(q):
    x = int(readline())
    #print(a_list)
    print(fab(n,a_list,x))