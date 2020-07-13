n = int(input())
A = list(map(int, input().split()))
res = {}
for i in A:
    res[i] = res.get(i, 0) + 1
print(1 if max(res.values()) > n/2 else 0)