import java.util.*

fun main(args: Array<String>) {


    val reader = Scanner(System.`in`);

    val x: Double = reader.nextDouble()
    val y: Double = reader.nextDouble()
    if (x == 0.0 && y == 0.0) {
        println("Origem")
    } else if (x == 0.0) {
        println("Eixo Y")
    } else if (y == 0.0) {
        println("Eixo X")
    } else if (y > 0 && x > 0) {
        println("Q1")
    } else if (y > 0 && x < 0) {
        println("Q2")
    } else if (y < 0 && x < 0) {
        println("Q3")
    } else if (y < 0 && x > 0) {
        println("Q4")
    }
}



//val nome = readLine()
//println("TOTAL = R$ ${String.format("%.2f",final)}")


/*
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplo de Entrada	Exemplo de Saída
4.5 -2.2

Q4

0.1 0.1

Q1

0.0 0.0

Origem
*/