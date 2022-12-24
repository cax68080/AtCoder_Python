from sys import stdin
readline = stdin.readline
list_s = list(readline().rstrip('\n'))
count_kakko = 0
j = 0
list_str = [[]]
result = "Yes"
#print(list_s)
for i in range(len(list_s)):
    if list_s[i] == "(":
        list_str.append([])
        count_kakko += 1
    elif list_s[i] == ")":
        list_str[count_kakko] = []
        count_kakko -= 1 
    else:
        for j in list_str:
            if list_s[i] in j:
                result = "No"
                break
        if result == "No":
            break
        else:
            list_str[count_kakko].append(list_s[i])
        #print(list_str)
print(result)

