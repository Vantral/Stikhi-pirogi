import telebot
from poet import Poem
import numpy as np
import json
import time
import instruments.db_operator as db
from threading import Thread
from bot_token import TOKEN     #put your token into bot_token.py

bot = telebot.TeleBot(TOKEN)
poem = Poem()
periodical_poem = Poem()
db.__init__()

with open("dictionaries/first_words_perc.json", 'r', encoding="utf-8") as f:
    first_words = json.load(f)

with open("dictionaries/first_bigrams_perc.json", 'r', encoding="utf-8") as f:
    first_bigrams = json.load(f)


def send_post(minutes=1):
    while True:
        time.sleep(minutes*20)

        periodical_poem.generate_token("unigram", np.random.choice([x for x in first_words.keys()], 1, [x for x in first_words.values()])[0])
        uni = periodical_poem.show()
        periodical_poem.clear()

        periodical_poem.generate_token("bigram", np.random.choice([x for x in first_bigrams.keys()], 1, [x for x in first_bigrams.values()])[0])
        bi = periodical_poem.show()
        periodical_poem.clear()

        periodical_poem.generate_markov()
        mark = periodical_poem.show()
        periodical_poem.clear()

        subs_message = f"/Униграмма/\n{uni}\n\n/Биграмма/\n{bi}\n\n/Марков/\n{mark}"

        for each in db.get_list():
            bot.send_message(each, subs_message)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет, я бот который пишет стихи пироги. Напиши /gen чтобы начать пользоваться
    \nИли напиши /sub чтобы получать пирожки каждый час (или /unsub когда надоест)""")

@bot.message_handler(commands=['sub'])
def subscribe(message):
    id = message.chat.id
    db.subscribe(id)
    bot.send_message(message.chat.id, "Вы подписались на ежечасную рассылку")

@bot.message_handler(commands=['unsub'])
def unsubscribe(message):
    id = message.chat.id
    db.unsubscribe(id)
    bot.send_message(message.chat.id, "Вы отписались от рассылки")
    

@bot.message_handler(commands=['gen'])
def send_request(message):
    mark_up = telebot.types.InlineKeyboardMarkup()
    item = telebot.types.InlineKeyboardButton(text='Генерация по униграмме', callback_data='1')
    mark_up.add(item)
    item = telebot.types.InlineKeyboardButton(text='Генерация по биграмме', callback_data='2')
    mark_up.add(item)
    item = telebot.types.InlineKeyboardButton(text='Генерация по маркову', callback_data='3')
    mark_up.add(item)
    bot.send_message(message.chat.id, 'Выбери генератор', reply_markup=mark_up)


@bot.callback_query_handler(func=None)
def send_response(message):
    if message.data == '1':
        poem.generate_token("unigram", np.random.choice([x for x in first_words.keys()], 1, [x for x in first_words.values()])[0])
    elif message.data == '2':
        poem.generate_token("bigram", np.random.choice([x for x in first_bigrams.keys()], 1, [x for x in first_bigrams.values()])[0])
    elif message.data == '3':
        poem.generate_markov()

    response = poem.show()
    bot.send_message(message.from_user.id, response)
    poem.clear()

th_timer = Thread(target=send_post)
th_timer.start()
bot.polling(none_stop=True)
