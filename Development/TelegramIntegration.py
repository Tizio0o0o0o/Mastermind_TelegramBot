import sys
import time
import telepot
import re

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text'].lower()

        print('Got command: %s' % command)

        if 'help' in command:
                bot.sendMessage(chat_id,str('Command list:\n-history: talks a little bit about the history of the game;\n-rules: explain how to play the game;\n-play: start new game.'))
        elif 'history' in command:
                bot.sendMessage(chat_id,str('The game is based on an older, paper based game called Bulls and Cows. A computer adaptation of it was run in the 1960s on Cambridge University\'s Titan computer system, where it was called \'MOO\'. This version was written by Frank King. There was also another version for the TSS/8 time sharing system, written by J.S. Felton and finally a version for the Multics system at MIT by Jerrold Grochow. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. Meirowitz presented the idea to many major toy companies but, after showing it at the Nuremberg International Toy Fair, it was picked up by a plastics company, Invicta Plastics, based near Leicester, UK. Invicta purchased all the rights to the game and the founder, Edward Jones-Fenleigh, refined the game further. It was released in 1971–2. Since 1971, the rights to Mastermind have been held by Invicta Plastics (Invicta always named the game Master Mind) They originally manufactured it themselves, though they have since licensed its manufacture to Hasbro worldwide, with the exception of Pressman Toys and Orda Industries who have the manufacturing rights to the United States and Israel, respectively. Starting in 1973, the game box featured a photograph of a man in a suit jacket seated in the foreground, with a young Asian woman standing behind him. The two amateur models (Bill Woodward and Cecilia Fung) reunited in June 2003 to pose for another publicity photo.'))
#                bot.sendPhoto(chat_id,open('./Box1.png','rb'))
        elif 'rules' in command:
                bot.sendMessage(chat_id,str('I\'m the codemaker, and you the codebreaker. The codemaker chooses a pattern of n elements(you decide how many). Player decide in advance whether duplicates are allowed. If so, the codemaker may even choose four same-number code. The codebreaker tries to guess the pattern within eight to twelve turns. Each guess is made by sending a code. Once sent, the codemaker provides feedback by saying how many correct number in correct position (Correct) and correct number in incorrect position (Reposition) are in the guess. If there are duplicate numbers in the guess, they cannot all be awarded unless they correspond to the same number of duplicate numbers in the hidden code. For example, if the hidden code is 1-1-2-2 and the player guesses 1-1-1-2, the codemaker will award two \"Correct\" for the two correct 1, nothing for the third 1 as there is not a third 1 in the code, and a \"Reposition\" for the 2. No indication is given of the fact that the code also includes a second 2. Once feedback is provided, another guess is made; guesses and feedback continue to alternate until either the codebreaker guesses correctly, or all turns of guest are used.\nGood luck ;)'))
        elif 'play' in command:
                bot.sendMessage(chat_id,str('Ok, let\'s start a new game.'))
                bot.sendMessage(chat_id,str('Firstly choose how many number I can choose the combination from (5 to 10,default 6), how long is the combination (3 to 6, default 4), how many rounds you have to crack my code (8 to 12, default 9) and if colors can be repeted (1 for yes or 0 for no, default 0)\nex:'))
                bot.sendMessage(chat_id,str('Settings:\nNumbers=6\nCode length=4\nTurns=9\nNo'))
        elif 'settings' in command:
                res=[re.findall(r'=(\w+)', command)]

                number=int(res[0][0])
                row=int(res[0][1])
                rounds=int(res[0][2])
                repetition=int(res[0][3])
                
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
                bot.sendMessage(chat_id,str('By the way, good lack, I already generated my secret code'))

bot = telepot.Bot('TOKEN')
bot.message_loop(handle)
print('I am listening...')

while 1:
        try:
                time.sleep(10)
        except KeyboardInterrupt:
                exit()
        except:
                print('Boh error')
