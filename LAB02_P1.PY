#-- Faça um programa em Python que leia uma matriz 4 x 4. Mostre a matriz recebida,
#-- e escreva quantos valores maiores que 10 ela possui.
peTra = []
panTone = []
contador = 0
for i in range(4):
    for j in range(4):
        panTone.append(int(input('LINHA: %d | COLUNA: %d: ' %(i, j))))
    peTra.append(panTone)
    panTone = []

for i in peTra:
    for j in i:
        if j > 10:
            contador = contador + 1

print(peTra)
print('Existem %d números > 10 na matriz informada! ' %(contador))