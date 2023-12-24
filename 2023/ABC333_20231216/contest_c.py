from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
for i in range(n):
    if i == 0:
        num_1 = "1"
        num_2 = "1"
        num_3 = "1"
    else:
        if len(num_1) == len(num_2) and len(num_1) == len(num_3):
            num_1 += "1"
            num_2 = "1"
            num_3 = "1"
        elif len(num_1) > len(num_2) and len(num_2) == len(num_3):
            num_2 += "1"
            num_3 = "1"
        elif len(num_1) > len(num_2) and len(num_2) > len(num_3):
            num_3 += "1"
        elif len(num_1) == len(num_2) and len(num_2) > len(num_3):
            num_3 += "1"
        else:
            pass
    #print(num_1,"",num_2,"",num_3)
print(int(num_1) + int(num_2) + int(num_3))