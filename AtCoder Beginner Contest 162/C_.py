import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


K = int(input())
gcdsum = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            print(str(gcd(a, b, c))+', a:'+str(a)+', b:'+str(b)+', c:'+str(c))
            gcdsum += int(gcd(a, b, c))
print(gcdsum)
