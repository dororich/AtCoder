# 回数
N = int(input())
# 入力Ai
A = list(map(int, input().split()))
ans = float('inf')

# 2進数にして数の右から0が続くぶんだけ2で割れる
# 20 = 10100 -> 20-10-5 = 2回
# (全部の長さ)-(右から検索して1が出るまでの長さ)-1 = (右から0が連続する数)
# 無限の下りはよくわからなかった
for i in A:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1)

print(round(ans))
