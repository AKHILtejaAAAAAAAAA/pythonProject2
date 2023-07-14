happiness = 0
n_and_m = input().split()
n = list(input().split())
a_num = set(input().split())
b_num = set(input().split())
for n in n:
    if n in a_num:
        happiness += 1
    elif n in b_num:
        happiness -= 1
    else:
        continue
    print(happiness)