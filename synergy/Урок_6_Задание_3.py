a = int(input("A: "))
b = int(input("B: "))
if a <= b:
    print("Четные в диапазоне от A до B: ")
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=' ')
else:
    print("Не выполнено условие 'A <= B'")
