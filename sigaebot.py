# -*- coding:utf-8 -*-
import sigaebot_private as bot_private
import importlist as code
import json

answer = ['ㅇㅇ', 'ㄴㄴ']

Anti_monday = False
thread_active = False
ct = 0
si = -1
bun = -1
hcnt = 0


def remove_none(text):
    if text is None:
        return ""
    else:
        return text



bot = code.telebot.TeleBot(bot_private.id['botid'])


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

@bot.message_handler(commands = ['search'])
def search_keyword(message):
    count = 0
    slicing_text =  message.text.replace("/search", "").split()
    bot.reply_to(message, '서칭시작')
    for i in range(0, message.message_id):
        try:
            forwardMessage = bot.forward_message(773884200, message.chat.id, i)
            if slicing_text[0] in forwardMessage.text and forwardMessage.forward_from.username.lower() == slicing_text[1].lower():
                count += 1
        except Exception:
            i += 1
    bot.reply_to(message, count)

@bot.message_handler(commands = ['test'])
def testf(message):
    bot.reply_to(message, bot.forward_message(message.from_user.id, message.chat.id, 517968).forward_from.username)


@bot.message_handler(commands = list(bot_private.quickcommand.keys()))
def quickcommand(message):
    bot.reply_to(message, bot_private.quickcommand[message.text[1:5]]())


@bot.message_handler(commands=['namu'])
def namuwiki(message):
    url = 'https://namu.wiki/w/{0}'.format(message.text.replace("/namu ", "").replace(" ","%20").strip())
    bot.send_message(message.chat.id, url)

@bot.message_handler(func=lambda Alwaystrue: True)
def always(message):
    print(message, end='\n\n')
    try:
        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value())
                return
        for key, value in bot_private.regex_username.items():
            if "죽인다" in message.text and key in message.text:
                
                with open('table.json', 'r') as fr:
                    json_str = json.loads(fr.read())

                killerName = message.from_user.username
                diedName = value
                json_str[0][killerName.lower()] += 1
                json_str[1][value.lower()] += 1
                print(json_str[0][killerName.lower()])
                print(json_str[1][value.lower()])
                print('temp')
                bot.send_message(message.chat.id,"{0}님께서 {1}님을 죽이셨습니다.\n{0}님의 킬카운트 : {2}\n{1}님의 데스카운트 : {3}".format(killerName, diedName, json_str[0][killerName.lower()],   json_str[1][value.lower()]))
                json_dmp = json.dumps(json_str)
                with open("table.json", 'w') as fa:
                     fa.write(json_dmp)
        if Anti_monday:
            for key, value in bot_private.ban.items():
                if key in message.text:
                    bot.send_message(message.chat.id, value)
                    if "a" in bot.get_chat_member(message.chat.id, message.from_user.id).status:
                        bot.send_message(message.chat.id, "관리자는 킥할수 없습니다")
                    else:
                        bot.kick_chat_member(message.chat.id, message.from_user.id)
        if "에반데" in message.text:
            global ct
            global si
            global bun
            dt = code.datetime.today()
            if ct == 0:
                si = dt.hour
                bun = dt.minute + 1
            ct += 1
            if ct == 3:
                if dt.minute <= bun and si == dt.hour:
                    bot.send_message(message.chat.id, "3진 에바로 기각되었습니다")
                    ct = 0
                else:
                    ct = 1
                si = dt.hour
                bun = dt.minute
            print(ct)
        if "자야지" in message.text and message.from_user.id == 222521602:
            global hcnt
            hcnt += 1
            bot.reply_to(message, hcnt)
    except Exception as e:
        print(e)


def tr():
    global thread_active
    thread_active = True
    code.time.sleep(30)
    thread_active = False

bot.polling()

