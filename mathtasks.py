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

task_answer = -1

def process_command_start():
    global task_answer
    
    a = randint(1,10)
    b = randint(1,10)

    task_answer = a+b

    return f"напишите ответ {a}+{b}=?"

def process_command_help():
    return "для загадывания нового примера нажмите /start"

def process_user_answer(request):
    if request.isdecimal() == True:
        user_number = int(request)
        if user_number == task_answer:
            response = "это правильный ответ, введите /start для генерации нового примера"
        else:
            response = "это НЕправильный ответ, подумай ещё или введи /start для генерации нового примера"
    else:
        response = "ошибка игры вы ввели не число, если хотите сгенерировать новый пример - введите /start"

    return response

def process_request(request):
    if request == '/start':
        response = process_command_start()
    elif request == '/help':
        response = process_command_help()
    else:
        response = process_user_answer(request)

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