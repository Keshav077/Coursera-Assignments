n = int(input())
A = list(map(int, input().split()))
max1, max2 = 0, 0
for i in range(n):
    if A[i] > max1:
        max2 = max1
        max1 = A[i]
    elif A[i] > max2:
        max2 = A[i]
print(max1 * max2)