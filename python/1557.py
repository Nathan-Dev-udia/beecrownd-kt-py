"""
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

Exemplo de Entrada	Exemplo de Saída
1

2

3

4

5

0

1

1 2
2 4

 1  2  4
 2  4  8
 4  8 16

 1  2  4  8
 2  4  8 16
 4  8 16 32
 8 16 32 64

  1   2   4   8  16
  2   4   8  16  32
  4   8  16  32  64
  8  16  32  64 128
 16  32  64 128 256
"""
n = 9999

while True:
    n = int(input())

    if n == 0:
        break
   
    m = list()



    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(0)



    m[0][0] = 1
    for i in range(0,n):
        if i >=1:
            m[i][0] = m[i - 1][0] * 2
           
        for j in range(1, n):
            m[i][j] = m[i][j-1] * 2


    T = len(str(m[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            m[i][j] = str(m[i][j])
            while len(m[i][j]) < T:
                m[i][j] = ' ' + m[i][j]
        M = ' '.join(m[i])
       
        print(M)
    print() 