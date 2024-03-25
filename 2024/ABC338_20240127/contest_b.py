from sys import stdin
readline = stdin.readline
s = str(readline().rstrip("\n"))
s_sort = sorted(s)
#print(s_sort)
letter_now = ""
letter_list = []
letter_count = 0
count_list = []
for i in s_sort:
    if letter_now == "":
        letter_now = i
        letter_count += 1
    elif letter_now == i:
        letter_count += 1
    elif letter_now != i:
        letter_list.append(letter_now)
        count_list.append(letter_count)
        letter_now = i
        letter_count = 1
    else:
        pass
letter_list.append(letter_now)
count_list.append(letter_count)
result = ""
diff = 0
#print(letter_list)
for i in range(len(letter_list)):
    if diff < count_list[i]:
        result = letter_list[i]
        diff = count_list[i]
print(result)
