from sys import stdin
readline = stdin.readline
a,b,c,d,e,f,x = map(int,readline().split())
#高橋と青木のa秒、d秒で歩く距離
tak_w = a * b
aok_w = d * e
#X秒で歩く→休憩を何回できるか？
tak_x = x // (a + c)
aok_x = x // (d + f)
#余りを求める
tak_z = x % (a + c)
aok_z = x % (d + f)
if tak_z < a:
    tak_result = tak_w * tak_x + b * tak_z
else:
    tak_result = tak_w * tak_x + tak_w
if aok_z < d:
    aok_result = aok_w * aok_x + e * aok_z
else:
    aok_result =  aok_w * aok_x + aok_w
if tak_result > aok_result:
    print("Takahashi")
elif aok_result > tak_result:
    print("Aoki")
else:
    print("Draw")