import os
import telebot

bot = telebot.TeleBot("2061155292:AAE8-Jnrskr8yxZ-s6Zkml18e3zZKG7ntE4")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I'm Maleesha and Please Don't Enter This Bot If You don't have Password")

@bot.message_handler(commands=["acess"])
def send_message(message):
    bot.send_message(message, "https://wmaleesha.tech")

bot.polling()