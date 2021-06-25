import telebot

TELEGRAM_API_KEY = ""
bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! How it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, "Hey 😍, Hope you're doing great!!!😚")


@bot.message_handler(commands=['welcome'])
def welcome(message):
    bot.send_message(message.chat.id, "😊 Great to see u back!")


bot.polling()
