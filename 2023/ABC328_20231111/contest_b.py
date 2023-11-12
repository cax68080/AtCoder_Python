from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
d_list = list(map(int,readline().rstrip("\n").split()))
str_month = ""
str_day = ""
count_day = 0
for i in range(1,n+1) :
    str_month = str(i)
    if len(str_month) == 2:
        if str_month[0] == str_month[1]:
            for j in range(1,d_list[i - 1] + 1):
                str_day = str(j)
                if (str_month[0] == str_day) or (str_month == str_day):
                    #print(str_month,str_day)
                    count_day += 1
    elif len(str_month) ==3:
        pass
    else:
        for j in range(1,d_list[i - 1] + 1):
            str_day = str(j)
            if len(str_day) == 2:
                if str_day[0] == str_day[1]:
                    if str_month == str_day[0]:
                        #print(str_month,str_day)
                        count_day += 1
            else:
                if str_month == str_day:
                    #print(str_month,str_day)
                    count_day += 1
print(count_day)





