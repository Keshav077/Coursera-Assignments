N = int(input())
i = 1
result = []
while N >= i:
    result.append(i)
    N -= i
    i += 1
result[-1] += N
print(len(result))
print(" ".join(map(str,result)))
