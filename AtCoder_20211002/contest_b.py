from sys import stdin
readline = stdin.readline
def fab(s,t):
    cnt = 0
    result = "Yes"
    list_s = list(s)
    list_t = list(t)
    se = ""
    for i in range(len(list_s)):
        if list_s[i] != list_t[i]:
            cnt += 1
            se = list_s[i]
            list_s[i] = list_s[i+1]
            list_s[i+1] = se
            if list_s[i] != list_t[i]:
                result = "No"
                break
        if cnt > 1:
            result = "No"
            break
        #print(s[i])
        #print(t[i])
        #print(cnt)
    return result
s = str(readline())
t = str(readline())
if s == t:
    print("Yes") 
else:
    print(fab(s,t))
