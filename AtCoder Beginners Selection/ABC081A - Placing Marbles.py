all = list(input())
num = 0
for s in all:
    if int(s) == 1:
        num += 1
print(num)

print(all.count('1'))


# こちらでよい
print(input().count('!'))
