import sys
import time
import telepot
import re
from random import randint
import copy

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text'].lower()

        print('Got command: %s' % command)

        if 'help' in command:
                bot.sendMessage(chat_id,str('Command list:\n- History : talks a little bit about the history of the game;\n- Rules : explain how to play the game;\n- Play : start new game;\n- Guess X X X X : (the X are number of your current guess) is the way to tell me your guess while playing'))
        elif 'history' in command:
                bot.sendMessage(chat_id,str('The game is based on an older, paper based game called Bulls and Cows. A computer adaptation of it was run in the 1960s on Cambridge University\'s Titan computer system, where it was called \'MOO\'. This version was written by Frank King. There was also another version for the TSS/8 time sharing system, written by J.S. Felton and finally a version for the Multics system at MIT by Jerrold Grochow. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. Meirowitz presented the idea to many major toy companies but, after showing it at the Nuremberg International Toy Fair, it was picked up by a plastics company, Invicta Plastics, based near Leicester, UK. Invicta purchased all the rights to the game and the founder, Edward Jones-Fenleigh, refined the game further. It was released in 1971–2. Since 1971, the rights to Mastermind have been held by Invicta Plastics (Invicta always named the game Master Mind) They originally manufactured it themselves, though they have since licensed its manufacture to Hasbro worldwide, with the exception of Pressman Toys and Orda Industries who have the manufacturing rights to the United States and Israel, respectively. Starting in 1973, the game box featured a photograph of a man in a suit jacket seated in the foreground, with a young Asian woman standing behind him. The two amateur models (Bill Woodward and Cecilia Fung) reunited in June 2003 to pose for another publicity photo.'))
                bot.sendPhoto(chat_id,open('./Box1.png','rb'))
        elif 'rules' in command:
                bot.sendMessage(chat_id,str('I\'m the codemaker, and you the codebreaker. The codemaker chooses a pattern of n elements(you decide how many). Player decide in advance whether duplicates are allowed. If so, the codemaker may even choose four same-number code. The codebreaker tries to guess the pattern within eight to twelve turns. Each guess is made by sending a code. Once sent, the codemaker provides feedback by saying how many correct number in correct position (Correct) and correct number in incorrect position (Reposition) are in the guess. If there are duplicate numbers in the guess, they cannot all be awarded unless they correspond to the same number of duplicate numbers in the hidden code. For example, if the hidden code is 1-1-2-2 and the player guesses 1-1-1-2, the codemaker will award two \"Correct\" for the two correct 1, nothing for the third 1 as there is not a third 1 in the code, and a \"Reposition\" for the 2. No indication is given of the fact that the code also includes a second 2. Once feedback is provided, another guess is made; guesses and feedback continue to alternate until either the codebreaker guesses correctly, or all turns of guest are used.\nGood luck ;)'))
        elif 'play' in command:
                with open('logfile.txt', 'r') as file:
                        lines = file.readlines()
                found = False
                for line in lines:
                        if str(chat_id) in line:
                                found = True

                                numbers=[re.findall(r'=(\d+)', line)]
                                num=int(numbers[0][1])
                                tur=int(numbers[0][3])
                                rw=int(numbers[0][2])
                                rep=int(numbers[0][4])

                                # code generation
                                colors = []        
                                for i in range(num):
                                        colors.append(i)
                                combination = [0 for x in range(rw)]
                                for i in range(rw):
                                        c = randint(0, (len(colors)-1))
                                        combination[i] = colors[c]
                                        if rep == 0:
                                                colors.pop(c)
                
                                # save in logfile
                                with open('logfile.txt', 'r') as file:
                                        lines = file.readlines()
                                        for i,line in enumerate(lines):
                                                if str(chat_id) in line:
                                                    del lines[i]
                                                    break
                                lines.append('Chat_id=' + str(chat_id) + ', Numbers=' + str(num) + ', Row=' + str(rw) + ', Turns=' + str(tur) + ', Repetition=' + str(rep) + ', Guess remaining=' + str(tur) + ', Combination=' + str(combination) + ';\n')
                                with open('logfile.txt', 'w') as file:
                                        file.writelines(lines)

                                bot.sendMessage(chat_id,str('Ok, let\'s start a new game, good lack. I already generated my secret code'))
                                break
                if not found:
                        bot.sendMessage(chat_id,str('Firstly choose how many number I can choose the combination from (5 to 10,default 6), how long is the combination (3 to 6, default 4), how many rounds you have to crack my code (8 to 12, default 9) and if colors can be repeted (1 for yes or 0 for no, default 0)\nIf you want to apply defoult settings just write:'))
                        bot.sendMessage(chat_id,str('Settings:\nNumbers=0\nCode length=0\nTurns=0\nRepetition=0'))
                        bot.sendMessage(chat_id,str('otherwise substitute the numers you prefer. You can change this settings every time you want, by sending same command'))
        elif 'solution' in command:
                with open('logfile.txt', 'r') as file:
                        lines = file.readlines()
                for i,line in enumerate(lines):
                        if str(chat_id) in line:
                                numbers=[re.findall(r'(\d+)', line)]
                                if len(numbers[0]) < 6:
                                        bot.sendMessage(chat_id,str('What solution are you talking about? You firt need to starte a new game, write \"play\" to start'))
                                        return
                                rw=int(numbers[0][2])
                                comb = [0 for x in range(rw)]
                                for j in range(rw):
                                        comb[j]=int(numbers[0][6+j])
                                combinazione = copy.deepcopy(comb)
                                bot.sendMessage(chat_id,str(combinazione))
                                return
        elif 'settings' in command:
                res=[re.findall(r'(\d+)', command)]
                if len(res[0]) != 4:
                        bot.sendMessage(chat_id,str('You have to tell me how many number I can choose the combination from (5 to 10,default 6), how long is the combination (3 to 6, default 4), how many rounds you have to crack my code (8 to 12, default 9) and if colors can be repeted (1 for yes or 0 for no, default 0)\nIf you want to apply default settings just write:'))
                        bot.sendMessage(chat_id,str('Settings:\nNumbers=0\nCode length=0\nTurns=0\nRepetition=0'))
                        bot.sendMessage(chat_id,str('otherwise substitute the numers you prefer'))
                        return
                number=int(res[0][0])
                row=int(res[0][1])
                turns=int(res[0][2])
                repetition=int(res[0][3])

                if number == 0:
                        number = 6
                elif number<5 or number>10:
                        bot.sendMessage(chat_id,str('Sorry, \"Numbers\" value needs to be from 5 to 10 (or 0 to use default settings of 6)'))
                        return
                if row == 0:
                        row = 4
                elif row<3 or row>6:
                        bot.sendMessage(chat_id,str('Sorry, \"Code length\" value needs to be from 3 to 6 (or 0 to use default settings of 4)'))
                        return
                if turns == 0:
                        turns = 9
                elif turns<8 or turns>12:
                        bot.sendMessage(chat_id,str('Sorry, \"Turns\" value needs to be from 8 to 12 (or 0 to use default settings of 9)'))
                        return
                if repetition!=0 and repetition!=1:
                        bot.sendMessage(chat_id,str('Sorry, \"Repetition\" value needs to be from 0 or 1 (0 for NOT allowed and 1 for allowed)'))
                        return

                with open('logfile.txt', 'r') as file:
                        lines = file.readlines()
                for i,line in enumerate(lines):
                        if str(chat_id) in line:
                                del lines[i]
                                break
                lines.append('Chat_id=' + str(chat_id) + ', Numbers=' + str(number) + ', Row=' + str(row) + ', Turns=' + str(turns) + ', Repetition=' + str(repetition) + ';\n')
                with open('logfile.txt', 'w') as file:
                        file.writelines(lines)


                if number==6 and row==4:
                        bot.sendMessage(chat_id,str('So, you are a tradicionalist, you like the original version from 1972! (me too ;P). Actually some newer ones have same settings: \'Mini Mastermind\' (1976,1988,2004), \'Number Mastermind\' (1976), \'Travel Mastermind\' (1988), \'Electronic Hand-Held Mastermind\' (1997)'))
                elif number==10 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Beagels\' (1972) and \'Royale Mastermind\' (1972)  and \'Electronic Mastermind\' (1977) and \'Super-Sonic Electronic Mastermind\' (1979)'))
                elif number==6 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Mastermind44\' (1972)'))
                elif number==10 and row==4:
                        bot.sendMessage(chat_id,str('This version is called \'Grand Mastermind\' (1974) and \'Electronic Mastermind\' (1977) and \'Super-Sonic Electronic Mastermind\' (1979)'))
                elif number==8 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Super Mastermind\' (1972) and \'Deluxe Mastermind\' (1972) and \'Advanced Mastermind\' (1972) and \'Mastermind Challenge\' (1993)'))
                elif number==10 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Electronic Mastermind\' (1977) and \'Super-Sonic Electronic Mastermind\' (1979)'))
                elif number==10 and row==6:
                        bot.sendMessage(chat_id,str('This version is called \'Super-Sonic Electronic Mastermind\' (1979)'))
                elif number==5 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Walt Disney Mastermind\' (1978'))
                elif number==8 and row==4:
                        bot.sendMessage(chat_id,str('This version is called \'Parker Mastermind\' (1993) and \'New Mastermind\' (2004)'))
                elif number==6 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Mastermind for Kids\' (1996)'))
                else:
                        bot.sendMessage(chat_id,str('That\'s a new version of mastermind, maybe you are the inventor, who knows'))
        elif 'guess' in command:
                with open('logfile.txt', 'r') as file:
                        lines = file.readlines()
                for i,line in enumerate(lines):
                        if str(chat_id) in line:
                                numbers=[re.findall(r'(\d+)', line)]
                                if len(numbers[0]) < 6:
                                        bot.sendMessage(chat_id,str('You firt need to starte a new game, write \"play\" to start or \"settings\" to change setings'))
                                        return
                                num=int(numbers[0][1])
                                tur=int(numbers[0][3])
                                rw=int(numbers[0][2])
                                rep=int(numbers[0][4])
                                guesstur=int(numbers[0][5])
                                comb = [0 for x in range(rw)]
                                for j in range(rw):
                                        comb[j]=int(numbers[0][6+j])
                                combinazione = copy.deepcopy(comb)
                                del lines[i]
                                break


                pla=[re.findall(r'(\d+)', command)]
                player = [0 for x in range(len(pla[0]))]
                for i in range(len(pla[0])):
                        player[i]=int(pla[0][i])

                if len(pla[0]) != rw:
                        bot.sendMessage(chat_id,str('You need to provide ' + str(rw) + ' numbers, not ' + str(len(pla[0])) + '!'))
                        return
                
                if guesstur > 0:
                        guesstur -= 1
                        corr = 0
                        pos = 0
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

                        if corr != rw:
                                bot.sendMessage(chat_id,str('Correct in correct position: ' + str(corr) + '\nCorrect in wrong position: ' + str(pos)))
                                lines.append('Chat_id=' + str(chat_id) + ', Numbers=' + str(num) + ', Row=' + str(rw) + ', Turns=' + str(tur) + ', Repetition=' + str(rep) + ', Guess remaining=' + str(guesstur) + ', Combination=' + str(comb) + ';\n')
                                with open('logfile.txt', 'w') as file:
                                        file.writelines(lines)
                        else:
                                bot.sendMessage(chat_id,str('Congratulation, you cracked my code. WELL DONE!'))
                                lines.append('Chat_id=' + str(chat_id) + ', Numbers=' + str(num) + ', Row=' + str(rw) + ', Turns=' + str(tur) + ', Repetition=' + str(rep) + ';\n')
                                with open('logfile.txt', 'w') as file:
                                        file.writelines(lines)

                else:
                        bot.sendMessage(chat_id,str('You finished your turns, I won xD my code was unbreakable'))
                        lines.append('Chat_id=' + str(chat_id) + ', Numbers=' + str(num) + ', Row=' + str(rw) + ', Turns=' + str(tur) + ', Repetition=' + str(rep) + ';\n')
                        with open('logfile.txt', 'w') as file:
                                file.writelines(lines)
        elif command == '/start':
                bot.sendMessage(chat_id,str('Hello, nice to meet you. I\'m Mind, Master Mind.\nDo you want to play with me? Tipe \"Help\" to begin'))
        else:
                bot.sendMessage(chat_id,str('Sorry, I didn\'t understand'))

bot = telepot.Bot('TOKEN')     #enter your bot token here
bot.message_loop(handle)
print('I am listening...')

while 1:
        try:
                time.sleep(10)
        except KeyboardInterrupt:
                exit()
        except:
                print('Random error')
