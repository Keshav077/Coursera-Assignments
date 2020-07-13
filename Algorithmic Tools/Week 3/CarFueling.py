d = int(input())
m = int(input())
n = int(input())
stop = list(map(int, input().split()))
stop.append(d)
prevStop, prevInd = 0, -1
result = 0
i = 0
while i <= n:
    # print(m, stop[i], prevStop)
    if m - stop[i] + prevStop < 0:
        if prevInd == i-1:
            print(-1)
            exit()
        prevInd = i-1
        prevStop = stop[i-1]
        result += 1
        continue
    i += 1
print(result)