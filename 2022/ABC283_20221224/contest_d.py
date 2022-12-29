from sys import stdin
from collections import defaultdict
readline = stdin.readline
list_s = list(readline().rstrip('\n'))
count_kakko = 0
j = 0
num = defaultdict(int)
dic = set()
list_str = [dic]
dic = set()
result = "Yes"
#print(list_s)
for i in range(len(list_s)):
    if list_s[i] == "(":
        list_str.append(dic)
        dic = set()
        count_kakko += 1
    elif list_s[i] == ")":
        for j in list_str[count_kakko]:
            num[j] = 0
        list_str[count_kakko] = set()
        count_kakko -= 1 
    else:
        if num[list_s[i]] == 1:
            result = "No"
            break
        else:
            list_str[count_kakko].add(list_s[i])
            num[list_s[i]] = 1
    #print(list_str)
    #print(num)
print(result)

