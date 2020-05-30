A, B, C, K = map(int, input().split())
ans = 0
if A >= K:
    ans += K
else:  # A < K
    if B >= (K - A):
        ans += A
    else:  # B< (K-A)
        if C >= (K - A - B):
            ans += A - (K-A-B)
        else:  # C < (K - A - B)
            ans += A - C
print(ans)
