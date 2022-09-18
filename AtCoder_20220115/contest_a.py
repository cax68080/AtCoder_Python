from sys import stdin
readline = stdin.readline
def fab(num):
    num_list = list(num)
    num1 = int(num_list[0] + num_list[1] +  num_list[2])
    num2 = int(num_list[1] + num_list[2] + num_list[0])
    num3 = int(num_list[2] + num_list[0] + num_list[1])
    return num1 + num2 + num3 
num = str(readline())
print(fab(num))
