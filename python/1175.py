"""
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

Exemplo de Entrada	Exemplo de Saída
0
-5
...
63
230

N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0
"""
N = []

for i in range(20):
    x=int(input())
    N.append(x)

a= N[::-1]

for j in range(20):
    
    print('N[{}] = {}'.format(j,a[j]))