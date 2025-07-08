import java.util.*

fun main(args: Array<String>) {


    val reader = Scanner(System.`in`);

    val DDD: Int = reader.nextInt()
    when (DDD) {
        61 -> println("Brasilia")
        71 -> println("Salvador")
        11 -> println("Sao Paulo")
        21 -> println("Rio de Janeiro")
        32 -> println("Juiz de Fora")
        19 -> println("Campinas")
        27 -> println("Vitoria")
        31 -> println("Belo Horizonte")
        
        else -> println("DDD nao cadastrado")
    }
}

/*
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:




Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
*/