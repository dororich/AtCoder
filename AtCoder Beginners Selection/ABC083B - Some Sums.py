# 入力
N, A, B = map(int, input().split())
ans = 0

for i in range(N + 1):
    # list(str(i))で文字列をリストにできる
    # 文字列の各桁をリストにして数値にして全部足して合計値を取る
    if A <= sum(list(map(int, list(str(i))))) <= B:
        ans += i
print(ans)
