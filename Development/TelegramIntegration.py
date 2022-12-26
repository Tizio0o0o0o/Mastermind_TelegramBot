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
                bot.sendMessage(chat_id,str('The game is based on an older, paper based game called Bulls'))
#                bot.sendPhoto(chat_id,open('./Box1.png','rb'))
        elif 'rules' in command:
                bot.sendMessage(chat_id,str('I\'m the codemaker, and you the codebreaker. The codemaker c'))
        elif 'play' in command:
                bot.sendMessage(chat_id,str('Ok, let\'s start a new game.'))
                bot.sendMessage(chat_id,str('Firstly choose how many number I can choose the combination '))
                bot.sendMessage(chat_id,str('Settings:\nNumbers=6\nCode length=4\nTurns=9\nNo'))
        elif 'settings' in command:
                res=[re.findall(r'=(\w+)', command)]

                number=int(res[0][0])
                row=int(res[0][1])
                rounds=int(res[0][2])
                repetition=int(res[0][3])
                
                if number==6 and row==4:
                        bot.sendMessage(chat_id,str('So, you are a tradicionalist, you like the original'))
                elif number==10 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Beagels\' (1972) and \'Roya'))
                elif number==6 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Mastermind44\' (1972)'))
                elif number==10 and row==4:
                        bot.sendMessage(chat_id,str('This version is called \'Grand Mastermind\' (1974) a'))
                elif number==8 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Super Mastermind\' (1972) a'))
                elif number==10 and row==5:
                        bot.sendMessage(chat_id,str('This version is called \'Electronic Mastermind\' (19'))
                elif number==10 and row==6:
                        bot.sendMessage(chat_id,str('This version is called \'Super-Sonic Electronic Mast'))
                elif number==5 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Walt Disney Mastermind\' (1'))
                elif number==8 and row==4:
                        bot.sendMessage(chat_id,str('This version is called \'Parker Mastermind\' (1993) '))
                elif number==6 and row==3:
                        bot.sendMessage(chat_id,str('This version is called \'Mastermind for Kids\' (1996'))
                else:
                        bot.sendMessage(chat_id,str('That\'s a new version of mastermind, maybe you are t'))
                bot.sendMessage(chat_id,str('By the way, good lack, I already generated my secret code'))

bot = telepot.Bot('5871967316:AAErxUPZf6gtSabIMfKYc2kJBMSBO4OdSi8')
bot.message_loop(handle)
print('I am listening...')

while 1:
        try:
                time.sleep(10)
        except KeyboardInterrupt:
                exit()
        except:
                print('Boh error')
