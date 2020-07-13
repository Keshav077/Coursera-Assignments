n = int(input())
A = list(map(int, input().split()))
res = []
maxi = str(max(A))
maxLen = len(maxi) + 1
for i in A:
    res.append((int((str(i)*maxLen)[:maxLen]), str(i)))
res.sort(reverse=True, key=lambda x: x[0])
ans = ""
for i in res:
    ans += i[1]
print(ans)