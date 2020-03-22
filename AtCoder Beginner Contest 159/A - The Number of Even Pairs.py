import math
N, M = map(int, input().split())
ans_ki = 0
ans_gu = 0
# 奇数奇数
if M > 1:
    ans_ki = (math.factorial(M) / (2 * math.factorial(M - 2)))
else:
    pass
# 偶数偶数
if N > 1:
    ans_gu = (math.factorial(N) / (2 * math.factorial(N - 2)))
else:
    pass
ans = round(ans_ki + ans_gu)
print(ans)
