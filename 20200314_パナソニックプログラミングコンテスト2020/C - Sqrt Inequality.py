import math

a, b, c = map(int, input().split())

if (2*math.sqrt(a)*math.sqrt(b)) < (c-a-b):
    print('Yes')
else:
    print('No')
