def is_snake_number(n):
    digits = list(map(int, str(n)))
    return all(digits[0] > d for d in digits[1:])

def count_snake_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        if is_snake_number(num):
            count += 1
    return count

# 使用例
from sys import stdin
readline = stdin.readline
l,r = map(int,readline().rstrip("\n").split())

result = count_snake_numbers(l, r)
print(result)
