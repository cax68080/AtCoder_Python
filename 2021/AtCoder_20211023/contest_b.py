from sys import stdin
readline = stdin.readline
def fab(h,w,a_list):
    result = "Yes"
    for i in range(h):
        for j in range(i,h):
            for k in range(w):
                for l in range(k,w):
                    if a_list[i][k] + a_list[j][l] <= a_list[j][k] + a_list[i][l]:
                        continue
                    else:
                        result = "No"
                        break
    return result
h,w = map(int,readline().split())
a_list = []
for i in range(h):
    a = []
    a = list(map(int,readline().split()))
    a_list.append(a)
#print(a_list)
print(fab(h,w,a_list))