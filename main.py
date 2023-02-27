import telebot
from random import randint
from datetime import datetime

# def log(message):
#     print(f"LOG {datetime.now()} --- {message}")

def log(message):
    f = open("log.txt","a")
    f.write(f"LOG {datetime.now()} --- {message}\n")
    f.close()

bot = telebot.TeleBot("6115585025:AAHDBAZYJkOvxmQxbO3b1jbhUqn1c_0GKL4")
log("BOT STARTED")

comp_number = -1

def process_guess_the_number(request):
    if request.isdecimal() == True:
        user_number = int(request)
        if user_number > comp_number:
            response = "введите поменьше"
        elif user_number < comp_number:
            response = "введите побольше"
        else:
            response = "вы угадали, введите /start для начала новой игры "
    else:
        response = "ошибка игры вы ввели не число для отгазывания, если хотите начать новую игру - введите /start"

    return response

@bot.message_handler(content_types=["text"])
def process_message(user_message):
    chat_id = user_message.chat.id
    request = user_message.text
    response = ""

    log(f"FROM {chat_id} received {request}")

    if request == '/start':
        global comp_number
        comp_number = randint(1,100)
        response = "бот загадал число от 1 до 100"
    elif request == '/help':
        response = "нажмите /start для начала новой игры"
    else:
        response = process_guess_the_number(request)

    bot.send_message(chat_id, response)

    log(f"TO {chat_id} send {response}")


bot.polling(none_stop=True, interval=0)