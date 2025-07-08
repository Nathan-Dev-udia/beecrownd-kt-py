"""
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

Exemplo de Entrada	Exemplo de Saída
5

0 1 1 2 3
"""
N  = int(input())

V1 = [0]*N

for i in range (0,N):
    
    if i <= 1:
        V1[i] = i
    
    else:
        V1[i] = V1[i-1] + V1[i-2]

    if i==N-1:
        print('%d'%(V1[i]),end='')
    
    else:
        print('%d'%(V1[i]),end=' ')
    
print()