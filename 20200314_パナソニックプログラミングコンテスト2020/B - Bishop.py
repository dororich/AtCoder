H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
elif H % 2 == 0:
    if W % 2 == 0:
        ans = H*(W//2)
    else:
        ans = H*((W-1)//2)+(H//2)
elif H % 2 == 1:
    if W % 2 == 0:
        ans = H*(W//2)
    else:  # W%2==1
        ans = H*((W-1)//2)+((H+1)//2)
print(ans)
