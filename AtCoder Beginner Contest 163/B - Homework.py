N, M = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)
if N < sum_A:
    ans = -1
else:
    ans = N-sum_A

print(ans)
