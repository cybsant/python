## ввод числа
source = int(input('5-значное число: '))
# "Разложение" числа на цифры
source_txt = str(source)
d1 = float(source_txt[0])
d2 = float(source_txt[1])
d3 = float(source_txt[2])
d4 = float(source_txt[3])
d5 = float(source_txt[4])
# print(d1, d2, d3, d4, d5)
# Операции
r0 = d4 ** d5
r1 = r0 * d3
r2 = d1 - d2
r3 = r1 // r2
## final
print(f'Результат:', r3)
