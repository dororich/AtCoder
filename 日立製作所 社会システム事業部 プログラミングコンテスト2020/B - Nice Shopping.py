A, B, M = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

# 割引券使わない
ans = min(A_list) + min(B_list)

# 割引券読み込み
for i in range(1, M + 1):
    x, y, c = map(int, input().split())
    price = A_list[x - 1] + B_list[y - 1] - c
    ans = min(ans, price)

print(ans)
