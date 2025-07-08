"""
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal Secundária da matriz, conforme ilustrado abaixo (área verde).




Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
S
1.0
0.0
-3.5
2.5
4.1
...

12.6
"""
m=[]
letra = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
c = 0
s = 0
cont = 0
for i in range(11,0,-1):
    c +=1
    for j in range(c,12):
        s += m[i][j]
        cont += 1

if letra == 'S':
    print('{}'.format(s))

if letra == 'M':
    med = s / cont
    print('{:.1f}'.format(med))