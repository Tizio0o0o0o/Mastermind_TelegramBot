import sys
import time
import telepot
import re
from random import randint
import configparser

# Leggi il token dal file config.ini
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['telegram']['token']

def send_help_message(chat_id):
    help_message = (
        "Command list:\n"
        "- History : talks a little bit about the history of the game;\n"
        "- Rules : explain how to play the game;\n"
        "- Play : start new game;\n"
        "- Guess X X X X : (the X are number of your current guess) is the way to tell me your guess while playing"
    )
    bot.sendMessage(chat_id, help_message)

def send_history_message(chat_id):
    history_message = (
        "The game is based on an older, paper based game called Bulls and Cows. A computer adaptation of it was run in the 1960s on Cambridge University's Titan computer system, where it was called 'MOO'. "
        "This version was written by Frank King. There was also another version for the TSS/8 time sharing system, written by J.S. Felton and finally a version for the Multics system at MIT by Jerrold Grochow. "
        "The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. Meirowitz presented the idea to many major toy companies but, after showing it at the Nuremberg International Toy Fair, it was picked up by a plastics company, Invicta Plastics, based near Leicester, UK. "
        "Invicta purchased all the rights to the game and the founder, Edward Jones-Fenleigh, refined the game further. It was released in 1971–2. Since 1971, the rights to Mastermind have been held by Invicta Plastics (Invicta always named the game Master Mind) They originally manufactured it themselves, though they have since licensed its manufacture to Hasbro worldwide, with the exception of Pressman Toys and Orda Industries who have the manufacturing rights to the United States and Israel, respectively. "
        "Starting in 1973, the game box featured a photograph of a man in a suit jacket seated in the foreground, with a young Asian woman standing behind him. The two amateur models (Bill Woodward and Cecilia Fung) reunited in June 2003 to pose for another publicity photo."
    )
    bot.sendMessage(chat_id, history_message)
    bot.sendPhoto(chat_id, open('./Box1.png', 'rb'))

def send_rules_message(chat_id):
    rules_message = (
        "I'm the codemaker, and you the codebreaker. The codemaker chooses a pattern of n elements(you decide how many). Player decide in advance whether duplicates are allowed. "
        "If so, the codemaker may even choose four same-number code. The codebreaker tries to guess the pattern within eight to twelve turns. Each guess is made by sending a code. "
        "Once sent, the codemaker provides feedback by saying how many correct number in correct position (Correct) and correct number in incorrect position (Reposition) are in the guess. "
        "If there are duplicate numbers in the guess, they cannot all be awarded unless they correspond to the same number of duplicate numbers in the hidden code. For example, if the hidden code is 1-1-2-2 and the player guesses 1-1-1-2, the codemaker will award two \"Correct\" for the two correct 1, nothing for the third 1 as there is not a third 1 in the code, and a \"Reposition\" for the 2. "
        "No indication is given of the fact that the code also includes a second 2. Once feedback is provided, another guess is made; guesses and feedback continue to alternate until either the codebreaker guesses correctly, or all turns of guest are used.\nGood luck ;)"
    )
    bot.sendMessage(chat_id, rules_message)

def start_new_game(chat_id):
    with open('logfile.txt', 'r') as file:
        lines = file.readlines()
    
    found = False
    for line in lines:
        if str(chat_id) in line:
            found = True
            numbers = re.findall(r'=(\d+)', line)
            num = int(numbers[0])
            tur = int(numbers[1])
            rw = int(numbers[2])
            rep = int(numbers[3])

            # code generation
            colors = list(range(num))
            combination = [0] * rw
            for i in range(rw):
                c = randint(0, len(colors) - 1)
                combination[i] = colors[c]
                if rep == 0:
                    colors.pop(c)
            
            # save in logfile
            with open('logfile.txt', 'w') as file:
                file.writelines(lines)
            break

    if not found:
        bot.sendMessage(chat_id, "No previous game found. Please start a new game.")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()

    print(f'Got command: {command}')

    if 'help' in command:
        send_help_message(chat_id)
    elif 'history' in command:
        send_history_message(chat_id)
    elif 'rules' in command:
        send_rules_message(chat_id)
    elif 'play' in command:
        start_new_game(chat_id)

# Initialize the bot with your token
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while True:
    time.sleep(10)