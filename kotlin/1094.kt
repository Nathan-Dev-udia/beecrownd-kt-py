import java.util.*


fun main(args: Array<String>) {
    val reader = Scanner(System.`in`)
    val input = Scanner(System.`in`)


    val casos: Int
    var quant: Int

    var total_cobaias = 0
    var quant_coelho = 0
    var quant_rato = 0
    var quant_sapo = 0
    var porcentagem_quant_coelho = 0f
    var porcentagem_quant_rato = 0f
    var porcentagem_quant_sapo = 0f
//f = conversão pra float

    var especie: String

    casos = input.nextInt()

    for (i in 1..casos) {
        quant = input.nextInt()
        especie = input.next()
        total_cobaias += quant

        if (especie == "C"){
            quant_coelho += quant
        } else if (especie == "R") {
            quant_rato += quant
        } else if (especie == "S") {
            quant_sapo += quant
        }

        porcentagem_quant_coelho = (quant_coelho * 100.00 / total_cobaias).toFloat()
        porcentagem_quant_rato = (quant_rato * 100.00 / total_cobaias).toFloat()
        porcentagem_quant_sapo = (quant_sapo * 100.00 / total_cobaias).toFloat()
    }

    print("Total: $total_cobaias cobaias\n")
    print("Total de coelhos: $quant_coelho\n")
    print("Total de ratos: $quant_rato\n")
    print("Total de sapos: $quant_sapo\n")

    System.out.printf("Percentual de coelhos: %.2f", porcentagem_quant_coelho)
    print(" %\n")
    System.out.printf("Percentual de ratos: %.2f", porcentagem_quant_rato)
    print(" %\n")
    System.out.printf("Percentual de sapos: %.2f", porcentagem_quant_sapo)
    print(" %\n")
}

//system.ou.printf = é usado para imprimir a saída na tela em Java.
//https://www.programiz.com/kotlin-programming/input-output outras opções


/*
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

Exemplo de Entrada	Exemplo de Saída
10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R

Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %
*/