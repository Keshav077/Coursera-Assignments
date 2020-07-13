N = int(input())
if N <= 1:
    print(N)
else:
    A = [0, 1]
    for i in range(1, N):
        A.append((A[-1] + A[-2]) % 10)
        A.pop(0)
    print(A[-1] % 10)
