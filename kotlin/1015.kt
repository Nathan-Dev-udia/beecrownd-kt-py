import java.util.*
import kotlin.math.abs

fun main(args: Array<String>) {


    val reader = Scanner(System.`in`);

    val x1: Double = reader.nextDouble()
    val y1: Double = reader.nextDouble()
    val x2: Double = reader.nextDouble()
    val y2: Double = reader.nextDouble()

    val distancia: Double = Math.sqrt(Math.pow((x2 - x1), 2.0) + Math.pow((y2 - y1), 2.0));




    println("${String.format("%.4f",distancia)}")


}

/*
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

Exemplo de Entrada	Exemplo de Saída
1.0 7.0
5.0 9.0

4.4721

-2.5 0.4
12.1 7.3

16.1484

2.5 -0.4
-12.2 7.0

16.4575
*/