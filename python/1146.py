"""
Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.

Obs: cuide para não deixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error.

Entrada
O arquivo de entrada contém vários números inteiros. O último número no arquivo de entrada é 0.

Saída
Para cada número N do arquivo de entrada deve ser impressa uma linha de 1 até N, conforme o exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

Exemplo de Entrada	Exemplo de Saída
5
10
3
0

1 2 3 4 5
1 2 3 4 5 6 7 8 9 10
1 2 3
"""
x=1
t=[]

while x != 0:
    x = int(input())
    
    for i in range(1, x + 1):
        t.append(i)
        t[i-1] = str(t[i-1])
        i = i + i
    t=' '.join(t)
    
    if x!= 0:      
        print(t)
        t =[]
