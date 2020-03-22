H, W = map(int, input().split())
if H == W:  # 正方形
    if H % 2 == 0 or W % 2 == 0:  # HとWが偶数
        ans = H * W // 2
    else:  # H=W=1も含まれる
        ans = (H * W + 1) // 2
else:  # 長方形
    if (H % 2 == 0) and (W % 2 == 0):  # 両方偶数
        ans = H * W // 2
    elif (H % 2 == 1) and (W % 2 == 1):  # 両者奇数
        ans = (H * W + 1) // 2
    else:  # 奇数と偶数、偶数と奇数
        ans = H * W // 2
print(ans)


elif W % 2 == 0:
    ans = (W // 2) * H
elif W % 2 == 1:
    if H % 2 == 0:
        ans = ((W - 1) // 2) * H + H // 2
    else:  # H%2==1
        ans = ((W - 1) // 2) * H + (H + 1) // 2
