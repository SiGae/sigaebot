# -*- coding:utf-8 -*-
import sigaebot_private as bot_private
import importlist as code
import dbconnect as db

answer = ['ㅇㅇ', 'ㄴㄴ']

Anti_monday = False
thread_active = False


def remove_none(text):
    if text is None:
        return ""
    else:
        return text



bot = bot_private.code.telebot.TeleBot(bot_private.id['botid'])


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
        for key0, value0 in bot_private.id.items():
            for key2, value2 in bot_private.regex.items():
                target_reg = code.re.compile(key2)
                if (target_reg.search(message.text) and value2 == key0)\
                        and "r" in bot.get_chat_member(message.chat.id, value0).status\
                        and message.from_user.id != value0:
                    bot.send_message(value0, "님 {}가 너 불러 \n 메세지 내용 : {}".format(
                                    str(message.from_user.first_name)
                                    + remove_none(message.from_user.last_name), message.text))
                    print("call")
        #for key, value in bot_private.banword.items():
            #if key in message.text:
                #bot.send_message(message.chat.id, message.text.replace(key,value))
                #bot.edit_message_text(message.text.replace(key,value),message.chat.id, message.message_id)
                #bot.delete_message(message.chat.id, message.message_id)
        for key, value in bot_private.command.items():
            if key in message.text:
                bot.reply_to(message, value())
                return
        for key, value in bot_private.regex_username.items():
            target_reg = code.re.compile(key)
            if "죽인다" in message.text and target_reg.search(message.text):
                killerName = message.from_user.namename
                diedName = value
                curs = db.conn.cursor()
                getKillCount = '' #kill_count 값을 가져오는 SQL 문 (SELECT 문 사용)
                killCount = curs.execute(getKillCount) + 1
                getDeathCount = '' #death_count 값을 가져오는 SQL 문 (SELECT 문 사용
                deathCount = curs.execute(getDeathCount) + 1
                #killCount변수의 값을 killName의 kill_count에 추가하는 구문 (UPDATE 문 사용)
                #deathCount변수의 값을 diedName의 death_count에 추가하는 구문 (UPDATE 문 사용)

                db.conn.close()


            #bot_private.kill_count+=1
            #bot.send_message(message.chat.id, "{0}의 킬카운트가 올라갔습니다\n현재 킬카운트 : {1}".format(message.from_user.first_name,bot_private.kill_count))
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


def tr():
    global thread_active
    thread_active = True
    code.time.sleep(30)
    thread_active = False

bot.polling()
