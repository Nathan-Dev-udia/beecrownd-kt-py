"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

Entrada
O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

Saída
Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

Exemplos de Entrada	Exemplos de Saída
JOAO
500.00
1230.30

TOTAL = R$ 684.54

PEDRO
700.00
0.00

TOTAL = R$ 700.00

MANGOJATA
1700.00
1230.50

TOTAL = R$ 1884.58
"""
nome = input()
salfixo = float(input())
qtdevendas = float(input())

bonus = float(qtdevendas * (15/100))

total = salfixo + bonus

print("TOTAL = R$ %0.2f" %total)
