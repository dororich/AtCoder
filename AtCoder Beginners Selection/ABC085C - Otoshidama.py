import sys
N, Y = map(int, input().split())
ans = None
for i in range(N + 1):
    for j in range(N - i + 1):
        if 10000 * i + 5000 * j + (N - i - j) * 1000 == Y:
            print(i, j, N - i - j)
            exit()

print('-1 -1 -1')
