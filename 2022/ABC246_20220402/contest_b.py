from sys import stdin
import math
readline = stdin.readline
a,b = map(int,readline().split())
c = math.sqrt(a ** 2 + b ** 2)
result_x = a / c
result_y = b / c
print(str(result_x) + " " + str(result_y))
