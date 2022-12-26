from random import randint


def main():
    colors = []
    player = []
    row = int(input("Numero di elementi della combinazione: "))
    turns = int(input("Numero di turni (0 per default): "))
    number = int(input("Numero di colori: "))

    for i in range(number):
        el = input("-- ")
        colors.append(el)

    combinazione = [0 for x in range(row)]

    for i in range(row):
        c = randint(0, (len(colors)-1))
        combinazione[i] = colors[c]
        colors.pop(c)

    if turns == 0:
        turns = 9

    while turns > 0:
        for i in range(row):
            el = input("-- ")
            player.append(el)

        check(combinazione, player)

        turns -= 1


def check(combinazione, player):
    corr = 0
    pos = 0
    # wrong = 0
    for i in range(len(player)):
        if player[i] in combinazione:
            if player[i] == combinazione[i]:
                corr += 1
            else:
                pos += 1
        # else:
        #     wrong += 1

    print("Corrette in posizione corretta: ", corr)
    print("Corrette in posizione sbagliata: ", pos)


main()
