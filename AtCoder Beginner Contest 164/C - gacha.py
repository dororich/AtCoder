N = int(input())
S = []
for _ in range(N):
    S.append(input())
S_s = list(set(S))
ans = len(S_s)

print(ans)
