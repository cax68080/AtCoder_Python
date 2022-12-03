from sys import stdin
readline = stdin.readline
def fab(n,a_list,a_max):
    r_list = [0 for i in range(n)]
    a = 0
    b = 0
    r = 0
    while a_max > a:
        a += 1
        b = 0
        r = 0
        while a_max > r:
            b += 1
            r = 4 * a * b + 3 * a + 3 * b
            #print(r)
            for i in range(len(a_list)):
                if a_list[i] == r:
                    r_list[i] = 1
    result = r_list.count(0)
    return result
n = int(readline())
a_list = list(map(int,readline().split()))
a_max = max(a_list)
print(fab(n,a_list,a_max))

