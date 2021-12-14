import telebot
import credentials
from telebot import types
name = ""
surname = ""
age = None
bot = telebot.TeleBot(credentials.TOKEN)
@bot.message_handler(commands=["start","help"])
def send(message):
    bot.reply_to(message, "how are you")

@bot.message_handler(func=lambda message: True)
def exo(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Привет! Давай познакомимся! Как тебя зовут?")
        bot.register_next_step_handler(message, reg_name)
    #bot.reply_to(message,message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    age = message.text
    try:
        age = int(message.text)
        bot.register_next_step_handler(message, reg_end)
    except Exception:
        bot.send_message(message.from_user.id, "Вводите цифры!")
        bot.register_next_step_handler(message, reg_age)


    #bot.register_next_step_handler(message, reg_end)

def reg_end(message):
    global age
    global name
    global surname
    statement ="Тебе" + str(age) + "и тебя зовут" + str(name) + str(surname)
    keyboard = types.InlineKeyboardMarkup()
    key_y = types.InlineKeyboardButton(text="Да", callback_data="yes")
    keyboard.add(key_y)
    key_n = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(key_n)
    bot.send_message(message.from_user.id, text=statement, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Данные записаны")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Давай познакомимся заново! Как тебя зовут?")
        bot.register_next_step_handler(call.message, reg_name)
bot.polling()