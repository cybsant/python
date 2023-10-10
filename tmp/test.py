a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(a)

for i in range(n):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = 