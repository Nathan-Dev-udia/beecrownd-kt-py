"""
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.

Exemplo de Entrada	Exemplo de Saída
3
0
4
2

Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
"""
t = int(input())

for i in range(t):
    x=int(input())
    f=[0,1]
    
    if x>1:
       
        for j in range(2,x+1):
           f.append(f[j-2]+f[j-1])
        
        print('Fib({}) = {}'.format(x,f[x]))
   
    if x <=1:
        
        print('Fib({}) = {}'.format(x,f[x]))