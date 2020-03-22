from collections import Counter
import math

N = int(input())
Al = list(map(int, input().split()))
d_di = {}
#d_in = {}
counter = Counter(Al)
As_l = list(set(Al))
for n in As_l:
    cnt = int(counter[n])
    if cnt > 1:
        d_di[n] = (math.factorial(cnt) // (2 * math.factorial(cnt - 2)))
    else:
        pass
#    if cnt > 2:
#        d_in[n] = (math.factorial(cnt-1) // (2 * math.factorial(cnt - 3)))
#    else:
#        d_in[n] = 1
# print(d_di)
# print(d_in)
total = sum(v for v in d_di.values())
for k in Al:
    ans = total - (counter[k]-1)
    if ans < 0:
        ans = 0
    else:
        pass
    print(ans)
