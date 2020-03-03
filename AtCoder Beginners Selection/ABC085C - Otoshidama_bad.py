N, Y = map(int, input().split())
money = 0
ans = None

for x in range(1, N):
    for y in range(1, N):
        for z in range(1, N):
            money = 10000 * x + 5000 * y + 1000 * z
            if money == Y and x+y+z == N:
                ans = str(x) + ' ' + str(y) + ' ' + str(z)
                break
        else:
            continue
        break
    else:
        continue
    break

if ans:
    print(ans)
else:
    print('-1 -1 -1')
