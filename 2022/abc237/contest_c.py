from sys import stdin
readline = stdin.readline
def fab(s):
    s_r = ""
    for i in range(len(s)):
        s_r = s[i] + s_r
    #print(s)
    #print(s_r)
    #return s_r
    if s == s_r:
        return "Yes"
    else:
        return "No"
s = str(readline().rstrip('\n'))
if list(s).count('a') == len(s):
    print("Yes")
elif s[0] != 'a' and s[-1] != 'a':
    if s[0] == s[-1]:
        print(fab(s))
    else:
        print("No")
elif s[-1] == 'a' and s[0] != 'a':
    r = 0 - len(s)
    cnt_a_e = 0
    for i in range(-1,r,-1):
        if s[i] == 'a':
            cnt_a_e += 1
        else:
            break
    s = 'a' * cnt_a_e + s
    #print(s)
    print(fab(s))
elif s[-1] != 'a' and s[0] == 'a':
    print("No")
elif s[-1] == 'a' and s[0] == 'a':
    r = 0 - len(s)
    cnt_a_e = 0
    for i in range(-1,r,-1):
        if s[i] == 'a':
            cnt_a_e += 1
        else:
            break
    cnt_a_s = 0
    for i in range(len(s)):
        if s[i] == 'a':
            cnt_a_s += 1
        else:
            break
    if cnt_a_e > cnt_a_s:
        s = 'a' * (cnt_a_e - cnt_a_s) + s
        print(fab(s))
    elif cnt_a_s == cnt_a_e:
        print(fab(s))
    else:
        print("No")
else:
    print("No")
        
        