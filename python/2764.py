"""
O seu professor gostaria de fazer um programa com as seguintes características:

Leia uma data no formato DD/MM/AA;
Imprima a data no formato MM/DD/AA;
Imprima a data no formato AA/MM/DD;
Imprima a data no formato DD-MM-AA.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem o seguinte formato DD/MM/AA onde DD, MM, AA são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme mostra o exemplo de saída a seguir.

Exemplos de Entrada	Exemplos de Saída
02/08/10

08/02/10

10/08/02

02-08-10

29/07/03

07/29/03

03/07/29

29-07-03
"""
while True:
    try:
        c = input()
        c = c.split('/')
        x = c[0]
        print('%s/%s/%s' %(c[1], c[0], c[2]))
        print('%s/%s/%s' %(c[2], c[1], c[0]))
        print('%s-%s-%s' %(c[0], c[1], c[2]))
       
    except EOFError:
        break