
A, B, C, D = map(int, input().split())

while A > 0 and C > 0:
    C = C - B
    A = A - D
    #print(C, A)

if A <= 0 and C <= 0:
    ans = 'Yes'
elif C <= 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
