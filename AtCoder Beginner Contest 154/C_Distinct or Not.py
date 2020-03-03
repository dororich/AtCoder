# 入力
n = int(input())
a_list = list(map(int, input().split()))


def has_duplicates(seq):
    return len(seq) != len(set(seq))


if has_duplicates(a_list):
    print('NO')
else:
    print('YES')
