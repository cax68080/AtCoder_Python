from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
while True:
  n_list = list(str(n))
  #print(n_list)
  if int(n_list[0]) * int(n_list[1]) == int(n_list[2]):
    print(n)
    break
  else:
    n += 1
    n_list = []

