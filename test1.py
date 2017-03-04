import telebot
import time
import urllib
import random
import database


def listener(messages):
    print(messages)
    for m in messages:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            msgid = m.message_id
            print(m.from_user, msgid, text)
            if text.startswith('/mong'):
                lst_id = database.select_db_option(table_name='thichngammong', field_selected='mong_id', condition='times_open < 1')
                lst_id = list(lst_id)
                print(lst_id)
                num = random.choice(lst_id)
                print(num)
                url = database.select_db_option(table_name='thichngammong', field_selected='mong_link', condition='mong_id = {mong_id}'.format(mong_id=num))
                url = url[0][0]
                f = open('out', 'wb')
                f.write(urllib.request.urlopen(url).read())
                f.close()

                tb.send_chat_action(chat_id, 'upload_photo')
                img = open('out', 'rb')
                tb.send_photo(chat_id, img)
                img.close()

                database.update_db(table_name='thichngammong', field_updated='times_open = times_open + 1', condition='mong_id = {mong_id}'.format(mong_id=num))


TOKEN = '366111923:AAG36kPTefdO74OPFAlmowYSmtGdnmcpo0Y'
tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener)  # register listener
tb.polling()

while True:
    time.sleep(1)
