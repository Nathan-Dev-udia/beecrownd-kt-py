"""
Como se sabe, existe um corvo com três olhos. O que não se sabia é que o corvo com três olhos pode prever o resultado da loteria de Westeros. Enquanto todos os outros corvos coletam as apostas, o corvo de três olhos já sabe o resultado, e quando Bran sonha com o corvo, o corvo conta o resultado. O problema é que Bran apesar de lembrar do sonho, não consegue interpretá-lo sozinho em tempo hábil. A sua tarefa é fazer um programa para interpretar o sonho de Bran e calcular o resultado da loteria.

Durante o sonho, o corvo pisca diversas vezes e grita apenas 3 vezes. A cada grito um número do resultado da loteria é calculado.

Cada piscada do corvo comunica um número em binário. Um olho aberto significa 1 e um olho fechado significa 0. O olho da esquerda é o mais significativo e o da direita é o menos significativo. A cada piscada, este número deve ser somado, e quando o corvo grita, essa soma é um resultado.

Entrada
A entrada descreve, em cada linha, em sequência, ou um grito ou uma piscada do corvo.

Um grito é representado pela string caw caw

Uma piscada é representada por três caracteres * ou -, representando, respectivamente, um olho aberto ou um olho fechado, da esquerda para a direita.

Lembre-se que o corvo tem 3 olhos.

Os números sorteados na loteria não excedem 1000.

Saída
A saída são três linhas, cada linha com um número da loteria.

Exemplo de Entrada	Exemplo de Saída
--*
caw caw
*--
caw caw
caw caw
1
4
0
Exemplo de Entrada	Exemplo de Saída
--*
--*
--*
caw caw
*--
*--
caw caw
--*
*--
caw caw
3
8
5
"""
def piscada_bin(piscada):
    piscada = piscada.replace('-','0')
    piscada = piscada.replace('*','1')
    return piscada


def bin_int(piscada):
    piscada = int(piscada,2)
    return piscada


def soma(piscada,s):
    s += piscada
    return s

def main():
    for i in range(3):
        s = 0
        while True:
            piscada = input()
            if piscada != 'caw caw':
                piscada = piscada_bin(piscada)
                piscada = bin_int(piscada)
                s = soma(piscada,s)
            else:
                print(s)
                break

main()
