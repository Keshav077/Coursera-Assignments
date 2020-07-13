import re
handle = open("actualData")
result = []
for line in handle:
    result.extend(re.findall("[0-9]+", line.rstrip()))
print(sum(map(int, result)))
