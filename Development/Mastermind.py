from random import randint


def main():
    colors = []
    player = []
    row = int(input("Numbers of elements of the combination (3 to 6,0 for default): "))
    turns = int(input("Number of turns (8 to 12,0 for default): "))
    number = int(input("Number of colors (5 to 10,0 for default): "))
    repetition = int(input("Can numbers be repeted in the combination? 1 to say yes or 0 to say no (0 for default): "))

    if row == 0:
        row = 4
    elif row<3 or row>6:
        print('cugghiuni')
        return        
    if turns == 0:
        turns = 9
    elif turns<8 or turns>12:
        print('cugghiuni')
        return
    if number == 0:
        number = 6
    elif number<5 or number>10:
        print('cugghiuni')
        return
    if repetition!=0 and repetition!=1:
        print('cugghiuni')
        return

    for i in range(number):
        colors.append(i)
    
    combinazione = [0 for x in range(row)]

    if repetition == 0:
        for i in range(row):
            c = randint(0, (len(colors)-1))
            combinazione[i] = colors[c]
            colors.pop(c)
    else:
        for i in range(row):
            c = randint(0, (len(colors)-1))
            combinazione[i] = colors[c]

    print(combinazione)
    
    while turns > 0:
        for i in range(row):
            el = int(input("-- "))
            player.append(el)

        check(combinazione, player)
        turns -= 1

def check(combinazione, player):
    corr = 0
    pos = 0

#    if repetition == 0
#        for i in range(len(player)):
#            if player[i] in combinazione:
#                if player[i] == combinazione[i]:
#                    corr += 1
#                else:
#                    pos += 1
#    else
    j = 0
    lun = len(player)
    for i in range(lun):
        if player[i-j] in combinazione:
            if player[i-j] == combinazione[i-j]:
                corr += 1
                player.pop(i-j)
                combinazione.pop(i-j)
                j += 1    
    for i in range(lun-j):
        if player[i] in combinazione:
            k = 0
            while player[i] != combinazione[k]:
                k += 1
            combinazione[k]=-1
            pos += 1

    print("Corrette in posizione corretta: ", corr)
    print("Corrette in posizione sbagliata: ", pos)


main()
