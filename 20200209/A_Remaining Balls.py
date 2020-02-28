# 入力
s, t = map(str, input().split())
# 数
a, b = map(int, input().split())
# 取るやつ
u = input()

if u == s:
    a -= 1
elif u == t:
    b -= 1

print(a, b)
