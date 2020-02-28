# 500円の枚数
A = int(input())
# 100円の枚数
B = int(input())
# 50円の枚数
C = int(input())
# 値段
X = int(input())

Y = 0
ans = 0

# 全部で回して計算してチェックする
for a in range(A+1):
    for b in range(B + 1):
        for c in range(C + 1):
            if a * 500 + b * 100 + c * 50 == X:
                ans += 1
print(ans)
