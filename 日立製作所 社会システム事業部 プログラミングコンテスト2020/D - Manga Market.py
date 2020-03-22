# ある店から最短で買えるもの
def min_store(t, s_i, ab, N):  # 現在の時刻, お店, お店リスト, お店数
    if N == 1:
        min_t = ab[0][0] * t + ab[0][1] + 1
        buy_j = 1
    elif s_i + 1 == N:
        min_t = ab[s_i - 1][0] * t + ab[s_i - 1][1] + 1  # s_iから一つ移動したお店での購入時間
        buy_j = s_i-1
    else:
        min_t = ab[s_i+1][0] * t + ab[s_i+1][1] + 1  # s_iから一つ移動したお店での購入時間
        buy_j = s_i+1
    t += 1
    for j in range(1, N):
        if t != 0:
            if ab[j][0] * t + ab[j][1] + 1 < min_t:
                min_t = ab[j][0] * t + ab[j][1] + t
                buy_j = j
        else:
            pass
    next_t = min_t
    return next_t, buy_j  # 購入後の時間, 買えたお店


N, T = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

buy = 0
t = 0
s_i = 0

while t < T+0.5:
    next_t, buy_j = min_store(t, s_i, ab, N)
    print(next_t, buy_j)
    t += next_t
    s_i = buy_j
    buy += 1
    #print(t, s_i)
buy -= 1
print(buy)
