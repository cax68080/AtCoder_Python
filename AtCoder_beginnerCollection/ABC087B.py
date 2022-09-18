from sys import stdin
readline = stdin.readline
cnt = 0
def makesmartChange(bills,target,highest,sol = []):
    global cnt
    if sum(sol) == target:
        #print(sol)
        cnt += 1
        return 
    if sum(sol) > target:
        return
    for bill in bills:
        if bill[0] >= highest:
            if bill[1] > sol.count(bill[0]):
                newSol = sol[:]
                newSol.append(bill[0])
                makesmartChange(bills,target,bill[0],newSol)
    return cnt
money_list = []
a = int(readline())
t = 500,a
money_list.append(t)
b = int(readline())
s = 100,b
money_list.append(s)
c = int(readline())
r = 50,c
money_list.append(r)
#print(money_list)
x = int(readline())
print(makesmartChange(money_list,x,50))
