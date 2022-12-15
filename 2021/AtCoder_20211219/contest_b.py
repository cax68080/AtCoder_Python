from sys import stdin
import string
readline = stdin.readline
def fab(list_a):
    list_result = []
    list_cnt = list(string.ascii_lowercase)
    for i in range(len(list_a)):
        if list_cnt.count(list_a[i]):
            list_result.append(list_cnt.index(list_a[i]))
    return list_result 
def fab2(list_s,list_t):
    s = 0
    result = "Yes"
    for i in range(len(list_s)):
        if i == 0:
            if list_s[i] > list_t[i]:
                s = list_t[i] - list_s[i] + 26
            else:
                s = list_t[i] - list_s[i]
        else:
            if list_s[i] > list_t[i]:
                if s == list_t[i] - list_s[i] + 26:
                    continue
                else:
                    result = "No"
                    break
            else:
                if s == list_t[i] - list_s[i]:
                    continue
                else:
                    result = "No"
                    break
    return result

list_s = list(str(readline()))
list_s = fab(list_s)
list_t = list(str(readline()))
list_t = fab(list_t)
print(fab2(list_s,list_t))

#print(list_s)
#print(list_t)

