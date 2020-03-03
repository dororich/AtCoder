import re
# 入力
s = input()
# 正規表現で置き換え
ans = re.sub(r'[a-z]', 'x', s)

print(ans)
