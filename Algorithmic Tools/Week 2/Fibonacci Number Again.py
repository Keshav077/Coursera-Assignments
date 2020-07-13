n, m = list(map(int, input().split()))
fibRem = [0, 1, 1]
search = [0, 1, 1]
found = False
while True:
    x = (fibRem[-1] + fibRem[-2]) % m
    fibRem.append(x)
    search.append(x)
    search.pop(0)
    if search == [0, 1, 1]:
        fibRem = fibRem[:-3]
        break
#print(fibRem)
n = n % len(fibRem)
print(fibRem[n])
