import math
A, B = map(int, input().split())

for i in range(1, 1011):
    n_a = math.floor(i * 0.08)
    n_b = math.floor(i * 0.1)
    if n_a == A and n_b == B:
        ans = i
        break
    ans = -1

print(ans)
