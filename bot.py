import telebot
from poet import Poem
from bot_token import TOKEN     #put your token into bot_token.py

bot = telebot.TeleBot(TOKEN)
poem = Poem()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот который пишет стихи пироги. Напиши /gen чтобы начать пользоваться')

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
        poem.generate_unigram()
    elif message.data == '2':
        poem.generate_bigram()
    elif message.data == '3':
        poem.generate_markov()

    response = poem.show()
    bot.send_message(message.from_user.id, response)
    poem.clear()

bot.polling(none_stop=True)
