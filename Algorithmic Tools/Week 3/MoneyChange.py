n = int(input())
coins = 0
while n > 0:
    if n >= 10:
        coins += n//10
        n %= 10
    if n >= 5:
        coins += n//5
        n %= 5
    if n >= 1:
        coins += n
        n = 0
print(coins)