# 入力
N = int(input())
cards = list(map(int, input().split()))
cards_sorted = sorted(cards, reverse=True)

alice = []
bob = []

for i in range(0, N):
    # 偶数(0,2,4)
    if i % 2 == 0:
        alice.append(cards_sorted[i])
    # 奇数(1,3,5)
    else:
        bob.append(cards_sorted[i])

# 合計値
alice_sum = sum(alice)
bob_sum = sum(bob)

#print(alice, bob)
ans = alice_sum - bob_sum

print(ans)
