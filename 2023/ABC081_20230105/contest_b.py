import sys

in_cntr = input()
in_data = input().split()
cntr = 0
ngflg = 0
dt_list = []
while ngflg == 0:
  for i in in_data:
    k = int(i)
    if k % 2 == 0:
      k = k / 2
      dt_list.append(k)
    else:
      ngflg = 1
      break
  if ngflg == 0:
    in_data = dt_list.copy()
    dt_list.clear()
    cntr += 1
print(cntr)


