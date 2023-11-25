from sys import stdin
readline = stdin.readline
s_list = list(readline().rstrip("\n"))
b_pos_1 = 0
b_pos_2 = 0
b_count = 0
result = "NO"
for i in range(8):
    if s_list[i] == "B":
        if b_count == 0:
            b_pos_1 = i
            b_count = 1
        else:
            b_pos_2 = i
#print(b_pos_1)
#print(b_pos_2)

if b_pos_1 % 2 == 0 and b_pos_2 % 2 != 0:
    result = "Yes"
elif b_pos_1 % 2 != 0 and b_pos_2 % 2 == 0:
    result = "Yes"
else:
    result = "No"
#print(result)
if result == "Yes":
    r_pos_1 = 0
    r_pos_2 = 0
    k_pos   = 0
    r_count = 0    
    for i in range(8):
        if s_list[i] == "R":
            if r_count == 0:
                r_pos_1 = i
                r_count = 1
            else:
                r_pos_2 = i
        elif s_list[i] == "K":
            k_pos = i
    if r_pos_1 < k_pos < r_pos_2:
        result = "Yes"
    else:
        result = "No"
print(result)
