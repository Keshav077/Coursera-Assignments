prev, curr = 0, 1
for i in range(1, 6+1):
    print(curr, end=" ")
    prev, curr = curr, prev + curr

