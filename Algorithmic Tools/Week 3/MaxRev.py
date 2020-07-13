n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
res = 0
for i in range(n):
    res += A[i] * B[i]
print(res)