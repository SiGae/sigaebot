# -*- coding:utf-8 -*-
import telebot
import time
import threading
import re
import sigaebot_private as bot_private

thread_active = False


def remove_none(text):
    if text is None:
        return ""
    else:
        return text


bot = telebot.TeleBot(bot_private.id['botid'])
memberlist = ["creator", "administrator", "member"]

@bot.message_handler(commands=['ping'])
def check_activate(message):
    bot.reply_to(message, "bot activation is stable ㄴ")
    bot.reply_to(message, bot.get_chat_member(message.chat.id, message.from_user.id))


def tr():
    global thread_active
    thread_active = True
    time.sleep(30)
    thread_active = False


@bot.message_handler(func=lambda alwaysTrue: True)
def alwaysTure(message):
    try:
        print(message, end='\n\n')
        for key0, value0 in bot_private.id.items():
            for key2, value2 in bot_private.regex.items():
                target_reg = re.compile(key2)
                if (target_reg.search(message.text) and value2 == key0)\
                        and "r" in bot.get_chat_member(message.chat.id, value0).status\
                        and message.from_user.id != value0:
                    bot.send_message(value0, "님 {}가 너 불러 \n 메세지 내용 : {}".format(
                                    str(message.from_user.first_name) + remove_none(message.from_user.last_name), message.text))
                    print("call")
                    return

#test
#        if "월요일" in message.text:
 #           bot.send_message(message.chat.id, "뭐? 월요일? 뒤지고 싶냐")
#            bot.kick_chat_member(message.chat.id,message.from_user.id )


        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value())
                return
            if "ㅋㅋㅋㅋㅋㅋㅋㅋ" in message.text:
                if not thread_active:
                    t = threading.Thread(target=tr)
                    bot.send_message(message.chat.id, 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
                    t.start()

    except Exception as e:
        print(e)

bot.polling()