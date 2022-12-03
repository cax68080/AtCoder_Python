from sys import stdin
readline = stdin.readline
def fab(h,w,n,r_list,c_list,a_list):
    cnt = 0
    result = ""
    for i in range(n):
        r = r_list[i]
        c = c_list[i]
        a = a_list[r-1][c-1]
        cnt = 0
        for i in range(h):
            if a < a_list[i][c-1]:
                cnt += 1
        for i in range(w):
            if a < a_list[r-1][i]:
                cnt += 1
        result = result + str(cnt) + " "
    return result
h,w,n = map(int,readline().split())
r_list = []
c_list = []
a_list = []
for i in range(w):
    a=[]
    a=[0]*h
    a_list.append(a)
#print(a_list)
for i in range(n):
    r=0
    c=0
    a=0
    r,c,a = map(int,readline().split())
    r_list.append(r)
    c_list.append(c)
    a_list[r-1][c-1] = a    
#for _ in range(n):
print(fab(h,w,n,r_list,c_list,a_list))