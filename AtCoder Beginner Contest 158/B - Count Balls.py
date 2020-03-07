N, A, B = map(int, input().split())

# Print(N / (A + B))
set_blue = A*(N // (A + B))

rem = N % (A + B)
if rem >= A:
    rem_blue = A
else:
    rem_blue = rem

print(set_blue + rem_blue)
