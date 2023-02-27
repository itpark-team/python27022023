import telebot
from random import randint
from datetime import datetime

def log(message):
    print(f"LOG {datetime.now()} --- {message}")

# def log(message):
#     f = open("log.txt","a")
#     f.write(f"LOG {datetime.now()} --- {message}\n")
#     f.close()

bot = telebot.TeleBot("6115585025:AAHDBAZYJkOvxmQxbO3b1jbhUqn1c_0GKL4")
log("BOT STARTED")

def process_command_start():
    f = open("jokes_db.txt", "r")
    jokes = f.readlines()

    random_joke_index = randint(0, len(jokes)-1)

    return jokes[random_joke_index]

def process_command_help():
    return "для выдачи случайно шутки нажмите /start"

def process_unknown_command():
    return "команда не распознана"

def process_request(request):
    if request == '/start':
        response = process_command_start()
    elif request == '/help':
        response = process_command_help()
    else:
        response = process_unknown_command()

    return response


@bot.message_handler(content_types=["text"])
def process_message(user_message):
    chat_id = user_message.chat.id
    request = user_message.text

    log(f"FROM {chat_id} received {request}")

    response = process_request(request)

    bot.send_message(chat_id, response)

    log(f"TO {chat_id} send {response}")


bot.polling(none_stop=True, interval=0)