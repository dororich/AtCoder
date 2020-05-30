import re

S = str(input())
T = str(input())

p = re.compile('[a-z]+')

if T.startswith(S):
    if p.fullmatch(T[-1]):
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'No'
print(ans)
