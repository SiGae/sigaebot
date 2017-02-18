# -*- coding:utf-8 -*-
import telebot
import time
import threading
import re
import sigaebot_private as bot_private

Anti_monday = True
thread_active = False


def remove_none(text):
    if text is None:
        return ""
    else:
        return text


bot = telebot.TeleBot(bot_private.id['botid'])


@bot.message_handler(commands=['ping'])
def check_activate(message):
    bot.reply_to(message, "bot activation is stable ")

@bot.message_handler(commands = bot_private.command1)
def i_dont_like_monday(message):
    global Anti_monday
    temp = message.text.replace("/kick", "").strip()
    if temp in bot_private.triggerOn:
        Anti_monday = True
        bot.send_message(message.chat.id, '켜짐 ㅎㅎ')
    elif temp in bot_private.triggerOff:
        Anti_monday = False
        bot.send_message(message.chat.id, '꺼짐ㅎㅎ')


def tr():
    global thread_active
    thread_active = True
    time.sleep(30)
    thread_active = False


@bot.message_handler(func=lambda Alwaystrue: True)
def alwaysTrue(message):
    try:
        print(message, end='\n\n')
        for key0, value0 in bot_private.id.items():
            for key2, value2 in bot_private.regex.items():
                target_reg = re.compile(key2)
                if (target_reg.search(message.text) and value2 == key0)\
                        and "r" in bot.get_chat_member(message.chat.id, value0).status\
                        and message.from_user.id != value0:
                    bot.send_message(value0, "님 {}가 너 불러 \n 메세지 내용 : {}".format(
                                    str(message.from_user.first_name)
                                    + remove_none(message.from_user.last_name), message.text))
                    print("call")

        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value())
                return
            if "ㅋㅋㅋㅋㅋㅋㅋㅋ" in message.text:
                if not thread_active:
                    t = threading.Thread(target=tr)
                    bot.send_message(message.chat.id, 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                    t.start()
        if Anti_monday:
            for key, value in bot_private.ban.items():
                if key in message.text:
                    bot.send_message(message.chat.id, value)
                    if "a" in bot.get_chat_member(message.chat.id, message.from_user.id).status:
                        bot.send_message(message.chat.id, "관리자는 킥할수 없습니다")
                else:
                    bot.kick_chat_member(message.chat.id, message.from_user.id)


    except Exception as e:
        print(e)


bot.polling()
