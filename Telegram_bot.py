import telebot
import credentials

bot = telebot.TeleBot(credentials.TOKEN)
@bot.message_handler(commands=["start","help"])
def send(message):
    bot.reply_to(message, "how are you")

@bot.message_handler(func=lambda message: True)
def exo(message):
    bot.reply_to(message,message.text)

bot.polling()
