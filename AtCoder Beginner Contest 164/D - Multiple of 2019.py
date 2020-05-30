import time
S = input()
S_int = int(S)
S_len = len(S)
ans1 = 0
ans2 = 0
t1 = time.time()
for i in range(0, S_len - 3):
    for j in range(4+i, S_len+1):
        S_ta = S[i:j]
        # print(S_ta)
        if int(S_ta) % 2019 == 0:
            ans1 += 1
            #print(i, j)
        else:
            pass


t2 = time.time()
for j in range(4, S_len):
    for i in range(0, S_len - 3):
        S_ta2 = S[i: i + j]
        # print(S_ta2)
        if int(S_ta2) % 2019 == 0:
            ans2 += 1
            #print(i, j)
        else:
            pass
        if i + j == S_len:
            break
        else:
            pass
t3 = time.time()
print(ans1, ans2)
Time1 = t2 - t1
Time2 = t3 - t2

print(Time1 > Time2)
print(Time1, Time2)
