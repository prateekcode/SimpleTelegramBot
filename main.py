import telebot
import requests
import random

TELEGRAM_API_KEY = ""
DAILY_SMARTY_BASE_URL = "http://api.dailysmarty.com/posts"

bot = telebot.TeleBot(TELEGRAM_API_KEY)
r = requests.get(DAILY_SMARTY_BASE_URL)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! How it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, "Hey 😍, Hope you're doing great!!!😚")


@bot.message_handler(commands=['welcome'])
def welcome(message):
    bot.send_message(message.chat.id, "😊 Great to see u back!")


r.json()
print(len(r.json()['posts']))


@bot.message_handler(commands=['blog'])
def micro_blog(message):
    for i in range(len(r.json()['posts'])):
        bot.send_message(message.chat.id, r.json()['posts'][i]['title'])


@bot.message_handler(commands=['small'])
def small_blog(message):
    random_post = random.randint(1, len(r.json()['posts']))
    message_to_sent = r.json()['posts'][random_post]['title'] + "\n\n" + r.json()['posts'][random_post]['content']
    bot.send_message(message.chat.id, message_to_sent)


bot.polling()
