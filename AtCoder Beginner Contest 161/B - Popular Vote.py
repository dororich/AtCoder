N, M = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
# print(A)
v_min = sum(A) / (4 * M)
# print(v_min)
cnt = 0
for item in A:
    if item >= v_min:
        cnt += 1
    else:
        break
if cnt >= M:
    print('Yes')
else:
    print('No')
