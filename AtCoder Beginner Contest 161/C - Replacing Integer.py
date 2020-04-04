N, K = map(int, input().split())
ans = int(N)
N_1 = N
N_2 = N
k_range = N // K
# print(k_range)

if k_range == 0:
    N = N - K
    if ans > abs(N):
        ans = abs(N)
else:
    N_1 = N - (K * k_range)
    N_2 = N - (K * (k_range + 1))

if abs(N_1) < abs(N_2):
    if ans > abs(N_1):
        ans = abs(N_1)
    else:
        pass
else:
    if ans > abs(N_2):
        ans = abs(N_2)
    else:
        pass
print(ans)
