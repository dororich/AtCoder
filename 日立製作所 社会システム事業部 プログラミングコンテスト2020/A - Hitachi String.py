S = input()
if len(S) != (S.count('h') + S.count('h')):
    print('No')
else:
    if S.count('h') == S.count('i') and S.count('i') == S.count('hi'):
        print('Yes')
    else:
        print('No')
