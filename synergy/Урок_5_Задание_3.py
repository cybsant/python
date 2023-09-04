X = int(input("Минимальная сумма: "))
A = int(input("Деньги Майкла: "))
B = int(input("Деньги Ивана: "))

if (A >= X) and (B >= X):
    Y = 2
elif (A >= X) and (B < X):
    Y = 'Mike'
elif (A < X) and (B >= X):
    Y = 'Ivan'
elif (A + B >= X):
    Y = 1
else:
    Y = 0

print("Результат:", Y)
