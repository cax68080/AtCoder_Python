from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
a_list = list(map(int,readline().rstrip("\n").split()))
#print(a_list)
result = 0
target = 10 ** 8
#def calc(x,y):
    #return (x + y) % target
#    return (x + y)
#for  i in range(n):
#    for j in range(i + 1,n):
        #print(calc(a_list[i],a_list[j]))
#        result += calc(a_list[i],a_list[j])
for  i in range(n):
        result += a_list[i]
print(result * (n - 1))