# """ Дано """
WORD = str(input("Введите слово: ").lower())
GL_CNT = 0
A_CNT = 0
E_CNT = 0
I_CNT = 0
O_CNT = 0
U_CNT = 0
SG_CNT = 0
NUM_CNT = 0
NUM_SRC = len(WORD)
# """ Считаем """
while NUM_CNT < NUM_SRC: # Пока не закончатся буквы
    if WORD[NUM_CNT] == 'a':
        GL_CNT += 1
        A_CNT += 1
    elif WORD[NUM_CNT] == 'e':
        GL_CNT += 1
        E_CNT += 1
    elif WORD[NUM_CNT] == 'i':
        GL_CNT += 1
        I_CNT += 1
    elif WORD[NUM_CNT] == 'o':
        GL_CNT += 1
        O_CNT += 1
    elif WORD[NUM_CNT] == 'u':
        GL_CNT += 1
        U_CNT += 1
    else:
        SG_CNT += 1
    NUM_CNT += 1
# """ Замена 0 на false """
if A_CNT == 0:
    A_CNT = 'False'
if E_CNT == 0:
    E_CNT = 'False'
if I_CNT == 0:
    I_CNT = 'False'
if O_CNT == 0:
    O_CNT = 'False'
if U_CNT == 0:
    U_CNT = 'False'
# """ Вывод """
print("Всего букв:", NUM_SRC)
print("Согласных:", SG_CNT)
print("Гласных:", GL_CNT)
print("A:", A_CNT)
print("E:", E_CNT)
print("I:", I_CNT)
print("O:", O_CNT)
print("U:", U_CNT)
