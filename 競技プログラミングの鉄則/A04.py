from sys import stdin
readline = stdin.readline
n = int(readline())
str_zero = "0"
str_one = "1"
answer = ""
while True:
    if n >= 2: 
        if n % 2 == 0:
            answer = str_zero + answer
        else:
            answer = str_one + answer
        n = n // 2
    elif n == 1:
        answer = str_one + answer
        #answer = str_zero + answer
        break
    else:
        pass
if len(answer) < 10:
   answer = "0" * (10 - len(answer)) + answer
print(answer)

