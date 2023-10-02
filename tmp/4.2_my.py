## ввод числа 
src = float(input('5-значное число: '))
## "Разложение" числа на цифры
src_txt = str(src)
d1 = float(src_txt[0])
d2 = float(src_txt[1])
d3 = float(src_txt[2])
d4 = float(src_txt[3])
d5 = float(src_txt[4])
print(d1, d2, d3, d4, d5)
## Операции
r0 = d4 ** d5
r1 = r0 * d3
r2 = d1 - d2
r3 = r1 // r2
## Вывод
print(r0, r1, r2)
print(f'Результат:', r3)
