import telebot
from datetime import datetime
import random
import time
import threading
import sigaebot_private as bot_private

thread_active = False


def tr():
    global thread_active
    thread_active = True
    time.sleep(30)
    thread_active = False


def remove_none(text):
    if text is None:
        return ""
    else:
        return text

answer = ['Yes', 'No']
bot = telebot.TeleBot(bot_private.id['botid'])


@bot.message_handler(commands=['pink'])
def check_activate(message):
    bot.reply_to(message, "bot activation is stable")


def todaytime() -> str:
    dt = datetime.today()
    text = '{0}시 {1}분 {2}초 '.format(dt.hour, dt.minute, dt.second)
    return text


@bot.message_handler(func=lambda alwaysTrue: True)
def alwaysTure(message):
    try:
        print(message, end='\n\n')
        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value)

    except Exception as e:
        print(e)

bot.polling()