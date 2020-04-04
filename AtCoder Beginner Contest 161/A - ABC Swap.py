X, Y, Z = map(int, input().split())
tmp = X
X = Y
Y = tmp

tmp_ = X
X = Z
Z = tmp_

print(X, Y, Z, sep=' ')
