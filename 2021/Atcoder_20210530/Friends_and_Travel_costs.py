from sys import stdin
readline = stdin.readline
def fab():
    n,k = map(int,readline().split())
    friend = []
    dic = {}
    a = []
    for i in range(n):
        a = list(map(int,readline().split()))
        friend.append(a)
    dic = dict(friend)
    #print(dic)
    for j in range(k):
        if j in dic:
            k += int(dic[j])
            print(k)
        print(j)
    return j
print(fab())
