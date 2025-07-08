import java.util.*

fun main(args: Array<String>) {

    val reader = Scanner(System.`in`);

    val num1: Int = reader.nextInt()
    val num2: Int = reader.nextInt()
    val num3: Int = reader.nextInt()
    val num4: Int = reader.nextInt()
    
    val soma = (num1 * num2) - (num3 * num4)

    println("DIFERENCA = $soma")

}

/*
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

Exemplos de Entrada	Exemplos de Saída
5
6
7
8

DIFERENCA = -26

0
0
7
8

DIFERENCA = -56

5
6
-7
8

DIFERENCA = 86
*/