from functools import reduce
import math


def gcd(*numbers):
    return reduce(math.gcd, numbers)


K = int(input())
gcdsum = K*K*K
gcd_ab = []
ab_list = []
for a in range(1, K + 1):
    for b in range(1, K + 1):
        #print(str(gcd(a, b))+', a:'+str(a)+', b:'+str(b))
        if gcd(a, b) != 1:
            ab_list.append(a)
            ab_list.append(b)
            gcd_ab.append(ab_list)
            ab_list = []
for ab in gcd_ab:
    ab = gcd(ab[0], ab[1])
    for c in range(1, K+1):
        if gcd(ab, c) != 1:
            #print(gcd(ab, c))
            gcdsum += gcd(ab, c)-1

print(gcdsum)
