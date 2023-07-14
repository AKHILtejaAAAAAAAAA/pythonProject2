from collections import Counter
n = int(input())
c = Counter()
for _ in range(n):
    str = input().split("\n")
    c.update(str)
print(len(list(c.keys())))
for i in c.values():
    print(i, end = " ")