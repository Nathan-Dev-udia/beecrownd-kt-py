import java.util.*

fun main(args: Array<String>) {

    val reader = Scanner(System.`in`);

    val a: Double = reader.nextDouble()
    val b: Double = reader.nextDouble()
    val c: Double = reader.nextDouble()

    val tri = (a*c)/2
    val circulo = 3.14159 * (c*c)
    val trapezio = ((a+b)*c)/2
    val quadrado = b*b
    val retangulo = a*b

    println("TRIANGULO: ${String.format("%.3f",tri)}")
    println("CIRCULO: ${String.format("%.3f",circulo)}")
    println("TRAPEZIO: ${String.format("%.3f",trapezio)}")
    println("QUADRADO: ${String.format("%.3f",quadrado)}")
    println("RETANGULO: ${String.format("%.3f",retangulo)}")

}


/*
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

Exemplos de Entrada	Exemplos de Saída
3.0 4.0 5.2

TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000

12.7 10.4 15.2

TRIANGULO: 96.520
CIRCULO: 725.833
TRAPEZIO: 175.560
QUADRADO: 108.160
RETANGULO: 132.080
*/