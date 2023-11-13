import random

n = 500
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
left_ind = 0
right_ind = n - 1
while left_ind <= right_ind:
    for i in range(left_ind, right_ind, +1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    right_ind -= 1
    for i in range(right_ind, left_ind, -1):
        if arr[i-1] < arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    left_ind += 1

#############################

print("Sorted:")
print(arr)
