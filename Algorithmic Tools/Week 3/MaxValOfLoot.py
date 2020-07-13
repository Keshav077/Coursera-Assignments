n, knapsack = list(map(int, input().split()))
values, weights = [], []
for i in range(n):
    X = list(map(int, input().split()))
    values.append(X[0])
    weights.append(X[1])
fractions = {}
for i in range(n):
    fractions[values[i] / weights[i]] = weights[i]
result = 0
for i in sorted(fractions.keys(), reverse=True):
    if fractions[i] > knapsack:
        result += knapsack * i
        break
    result += fractions[i] * i
    knapsack -= fractions[i]
print(round(result, 4))
