from sys import stdin
from decimal import Decimal, ROUND_HALF_UP
readline = stdin.readline
def fab(x):
    x = Decimal(x)
    result = x.quantize(Decimal('0'),rounding=ROUND_HALF_UP)
    return result
x = str(readline())
print(fab(x))