N = int(input())
fbsum = 0
for i in range(1, N+1):
    if i % 15 == 0:
        # print("Fizz Buzz!")
        pass
    elif i % 3 == 0:
        # print("Fizz!")
        pass
    elif i % 5 == 0:
        # print("Buzz!")
        pass
    else:
        # print(i)
        fbsum += i
print(fbsum)
