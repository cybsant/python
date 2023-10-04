def fctrl(n):
    if n <= 1:
        return 1
    else:
        return n * fctrl(n - 1)

n = int(input("Ввод числа: "))
fact_n = fctrl(n)
fact_list = [fctrl(i) for i in range(fact_n, 0, -1)]

print(f"Факториал [{n}]: {fact_n}")
print(f"Список факториалов [{fact_n}]: {fact_list}")
