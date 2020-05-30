S, W = map(int, input().split())
if W >= S:
    ans = 'unsafe'
else:
    ans = 'safe'
print(ans)
