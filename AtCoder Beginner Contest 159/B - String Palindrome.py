S = input()
L = len(S)
a = int((L - 1) / 2)
b = int((L+3)/2)
S_first = S[:a]
S_second = S[(b-1):]
if S_first == S_second[::-1]:
    L_2 = len(S_first)
    if L_2 % 2 == 1:  # 半分が奇数
        a_2 = int((L_2 - 1) / 2)
        b_2 = int((L_2 + 3) / 2)
        S_first_f = S_first[:a_2]
        S_first_s = S_first[(b_2 - 1):]
        if S_first_f == S_first_s[::-1]:
            print('Yes')
        else:
            print('No')
    else:  # 半分が偶数
        a_2 = int(L_2 / 2)
        b_2 = int((L_2 + 1) / 2)
        S_first_f = S_first[: a_2]
        S_first_s = S_first[(b_2):]
        if S_first_f == S_first_s[::-1]:
            print('Yes')
        else:
            print('No')
else:
    print('No')
