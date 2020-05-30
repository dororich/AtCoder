N, M, X = map(int, input().split())
str_list = []
for i in range(N):
    str_list.append(list(input().split()))
# print(str_list)
alg_ch = []
ch_ = 0
for j in range(1, M+1):
    alg = {}
    param = 0
    for i in range(N):
        param += int(str_list[i][j])
    if param >= X:
        alg[j] = 1
        ch_ += 1
    else:
        alg[j] = 0
    alg_ch.append(alg)
print(alg_ch)
if ch_ == M:  # 理解度は行ける

else:  # 理解度だめ
    ans = -1
