from sys import stdin
readline = stdin.readline
x1,y1,x2,y2 = map(int,readline().split())
result = "No"
for i in range(x1 - 2,x1 + 3):
    for j in range(y1 - 2,y1 + 3):            
        result1 = (i - x1) ** 2 + (j - y1) ** 2
        result2 = (i - x2) ** 2 + (j - y2) ** 2
        if result1 == result2 == 5:
            result = "Yes"
            break
    if result == "Yes":
        break
print(result)