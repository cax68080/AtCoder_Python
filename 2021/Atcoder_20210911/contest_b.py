from sys import stdin
readline = stdin.readline
def fab(p):
    result = ""
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in p:
        j = i - 1
        result = result + alpha[j]
    return result
p = list(map(int,readline().split()))
print(fab(p))

