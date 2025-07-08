import java.util.*

fun main(args: Array<String>) {


    val reader = Scanner(System.`in`);

    var segundosi: Int = reader.nextInt()
    
    val horas = segundosi / 3600
    segundosi -= horas * 3600
    val minutos = segundosi / 60
    segundosi -= minutos * 60
    val segundos = segundosi
    
    println("$horas:$minutos:$segundos")
}

/*
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
*/