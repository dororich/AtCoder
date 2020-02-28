# 入力
n, k = map(int, input().split())
p = list(map(int, input().split()))
ans_list = []

for i in range(n - k + 1):
    p_t = []
    for i in range(i + k):
        p_t.append(p[i])
    # 1個あたりの期待値
    p_all = sum(p_t)
    p_e = 0
    for p_ in p_t:
        p_e += p_ * (1 / p_all)
    ans = p_e * len(p_t)
    ans_list.append(p_e)

# 期待値*個数
ans = max(ans_list)
print(ans)
