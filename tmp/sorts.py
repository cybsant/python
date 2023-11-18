import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Notsorted:")
print(arr)
print("------")

#############################

### Bubble sort
# for i in range(n):
#     for j in range(n-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

### Shuffle sort
l_ind = 0
r_ind = n - 1
is_srt = True
while l_ind <= r_ind:
    for i in range(l_ind, r_ind, +1):
        if arr[i] < arr[i + 1]:
            is_srt = False
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    r_ind -= 1
    for i in range(r_ind, l_ind, -1):
        if arr[i-1] < arr[i]:
            is_srt = False
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    l_ind += 1
    if is_srt is True: # оптимизация лишних проходов
        break
    else:
        is_srt is True

#############################

print("Sorted:")
print(arr)
