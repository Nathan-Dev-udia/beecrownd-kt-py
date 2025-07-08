"""
No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas de Pedra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock.

As regras do jogo proposto são:

a tesoura corta o papel;
o papel embrulha a pedra;
a pedra esmaga o lagarto;
o lagarto envenena Spock;
Spock destrói a tesoura;
a tesoura decapita o lagarto;
o lagarto come o papel;
o papel contesta Spock;
Spock vaporiza a pedra;
a pedra quebra a tesoura.
Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não é difıcil deduzir o que aconteceria se a disputa continuasse. Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon.

Entrada
A entrada consiste em uma série de casos de teste. A primeira linha contém um inteiro positivo T (T ≤ 100), que representa o número de casos de teste. Cada caso de teste é representado por uma linha da entrada, contendo as escolhas de Sheldon e Raj, respectivamente, separadas por um espaço em branco. As escolha possíveis são as personagens do jogo: pedra, papel, tesoura, lagarto e Spock.

Saida
Para cada caso de teste deverá ser impressa a mensagem "Caso #t: R", onde t é o número do caso de teste (cuja contagem se inicia no número um) e R é uma das três reações possíveis de Sheldon: "Bazinga!", "Raj trapaceou!", ou "De novo!".

Exemplos de Entrada	Exemplos de Saída
3

papel pedra

lagarto tesoura

Spock Spock

Caso #1: Bazinga!

Caso #2: Raj trapaceou!

Caso #3: De novo!
"""
for i in range(int(input(""))):
    j1, j2 = input("").split()

    if j1 == j2:
        win = "De novo!"
    elif j1 == "pedra":
        if j2 == "tesoura" or j2 == "lagarto":
            win = j1
        else:
            win = j2
    elif j1 == "papel":
        if j2 == "pedra" or j2 == "Spock":
            win = j1
        else:
            win = j2
    elif j1 == "tesoura":
        if j2 == "lagarto" or j2 == "papel":
            win = j1
        else:
            win = j2
    elif j1 == "lagarto":
        if j2 == "Spock" or j2 == "papel":
            win = j1
        else:
            win = j2
    elif j1 == "Spock":
        if j2 == "tesoura" or j2 == "pedra":
            win = j1
        else:
            win = j2

    if win == j1:
        win = "Bazinga!"
    elif win == j2:
        win = "Raj trapaceou!"

    print("Caso #%i:" %(i + 1), win)