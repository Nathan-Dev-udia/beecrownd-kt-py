"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0

Area = 10.0

6.0 4.0 2.1

Perimetro = 12.1
"""
l1, l2, l3 = map(float, input().split())

if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    p = l1 + l2 + l3
    print('Perimetro = {:.1f}'.format(p))
    
else:
    at = ((l1+l2)*l3)/2
    print('Area = {:.1f}'.format(at))