n, *A = list(map(int, input().split()))
elements = {}
for i in range(n):
    elements[A[i]] = i
n, *A = list(map(int, input().split()))
res = [elements[i] if i in elements else -1 for i in A]
print(" ".join(map(str, res)))
