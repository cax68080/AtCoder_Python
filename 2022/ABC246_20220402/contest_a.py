from sys import stdin
readline = stdin.readline
x_list = []
y_list = []
for i in range(3):
    x,y = map(int,readline().split())
    x_list.append(x)
    y_list.append(y)
result_x = ""
result_y = ""
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        result_x = str(x_list[i])
    if y_list.count(y_list[i]) == 1:
        result_y = str(y_list[i])
print(result_x + " " + result_y)