"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplo de Entrada	Exemplo de Saída
4.5 -2.2

Q4

0.1 0.1

Q1

0.0 0.0

Origem
"""
x , y = map(float, input().split())

if x > 0 and y > 0:
    print('Q1')
    
if x < 0 and y > 0:
    print('Q2')
    
if x < 0 and y < 0:
    print('Q3')
    
if x > 0 and y < 0:
    print('Q4')
    
if y == 0 and x == 0:
    print('Origem')
    
if y == 0 and x != 0:
    print('Eixo X')
    
if x == 0 and y != 0:
    print('Eixo Y')