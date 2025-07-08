"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2
6 3
5 0

2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""
soma = 0
j=0

while j != 1:
    M,N = input().split(" ")
    M = int(M)
    N = int(N)
    soma = 0
    
    if M > N:
        aux = M
        M = N
        N = aux
    
    if M<=0 or N<=0:
        j = 1
    
    if j!=1:
        for i in range(M,N+1):
            print('%d '%(i),end="")
            soma+=i
            
            if i == N:
                print('Sum=%d'%(soma))