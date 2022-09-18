from sys import stdin
readline = stdin.readline
n = int(readline())
list_n = []
for i in range(n):
    list_d = list(map(int,readline().split()))
    #print(list_d)
    list_n.append(list_d)
    #list_d.clear()
list_s = list(str(readline().rstrip('\n')))
#print(list_n[1][1])
#print(list_s)
result = ""
for i in range(n):
    pos_1 = list_s[i]
    for j in range(i + 1,n):
        if pos_1 != list_s[j]:
            if list_n[j][1] == list_n[i][1]:
                if pos_1 == "R" and list_n[i][0] <= list_n[j][0]:
                    result = "Yes"
                    break
                elif pos_1 == "L" and list_n[i][0] >= list_n[j][0]:
                    result = "Yes"
                    break
                else:
                    continue
    if result == "Yes":
        print(result)
        break
if result == "":
    print("No")
    

