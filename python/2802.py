"""
Dado um conjunto de N pontos sobre uma circunferência de um círculo, todo par de pontos está ligado por um segmento e três desses segmentos nunca se encontram em um ponto interno à circunferência.

Sua tarefa é determinar em quantas partes esses segmentos dividem o interior do círculo.

Entrada
A primeira e única linha da entrada contém um inteiro N (1 ≤ N ≤ 1000) representando a quantidade de pontos sobre a circunferência.

Saída
A saída consiste de uma única linha contendo um inteiro representando a quantidade de partes do círculo.

Exemplos de Entrada	Exemplos de Saída
1

1

2

2

3

4

4

8

5

16
"""

n = int(input())
n = ((n/24.0)*(n**3 - 6*n*n + 23*n - 18)) + 1
print("%.0f" % n)