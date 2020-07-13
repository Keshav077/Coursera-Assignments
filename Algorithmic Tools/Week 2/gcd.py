a, b = sorted(list(map(int,input().split())))
while a != 0:
    tmp = a
    a = b % a
    b = tmp
print(b)