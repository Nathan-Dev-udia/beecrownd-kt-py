"""
A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

Entrada
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

Saída
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.

Exemplo de Entrada	Exemplo de Saída
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4

10/8 = 5/4
-2/8 = -1/4
12/18 = 2/3
4/6 = 2/3
"""
def opera(n1, d1, op, n2, d2):
    if op == '+':
        num = (n1 * d2) + (n2 * d1)
        dem = d1 * d2
    elif op == '-':
        num = (n1 * d2) - (n2 * d1)
        dem = d1 * d2
    elif op == '*':
        num = n1 * n2
        dem = d1 * d2
    elif op == '/':
        num = n1 * d2
        dem = n2 * d1
    return num, dem


def fatora(a, b):
    abs_a, abs_b = abs(a), abs(b)
    menor = min(abs_a, abs_b)
    maior = max(abs_a, abs_b)
    divisor = menor
    while divisor > 1:
        if (menor % divisor) == 0:
            if (maior % divisor) == 0:
                return int(a/divisor), int(b/divisor)
        divisor -= 1
    return a, b


testes = int(input())
for teste in range(0, testes):
    operacoes = input().strip().split(' ')
    n1, d1, op, n2, d2 = int(operacoes[0]), int(operacoes[2]), operacoes[3], int(operacoes[4]), int(operacoes[6])
    num, dem = opera(n1, d1, op, n2, d2)
    simp_num, simp_dem = fatora(num, dem)
    print('{}/{} = {}/{}'.format(num, dem, simp_num, simp_dem))
