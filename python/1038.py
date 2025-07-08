"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
3 2

Total: R$ 10.00

4 3

Total: R$ 6.00

2 3

Total: R$ 13.50
"""
cod, quant = map(int, input().split())

if cod == 1:
    total1 = 4*quant
    print('Total: R$ {:.2f}'.format(total1))
    
if cod == 2:
    total2 = quant*4.5
    print('Total: R$ {:.2f}'.format(total2))
    
if cod == 3:
    total3 = quant*5
    print('Total: R$ {:.2f}'.format(total3))
    
if cod == 4:
    total4 = quant*2
    print('Total: R$ {:.2f}'.format(total4))
    
if cod == 5:
    total5 = quant*1.5
    print('Total: R$ {:.2f}'.format(total5))