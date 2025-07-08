"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
556

0:9:16

1

0:0:1

140153

38:55:53
"""
s = int(input())

h = int(s/3600)
s = int(s - h*3600)

m = int(s/60)
s = int(s - m*60)

sf = int(m/60)
sf = s

print('{}:{}:{}'.format(h,m,sf))