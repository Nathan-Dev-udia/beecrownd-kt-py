import java.util.*
import kotlin.math.abs

fun main(args: Array<String>) {

    Locale.setDefault(Locale.US)

    val reader = Scanner(System.`in`);

    val a = reader.nextInt()
    val b = reader.nextInt()
    val c = reader.nextInt()

    val maior = ((a + b) + abs(a - b))  / 2
    val resultado = (maior + c + abs(maior - c)) / 2


    println("$resultado eh o maior")


}

/*
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	Exemplos de Saída
7 14 106

106 eh o maior

217 14 6

217 eh o maior
*/