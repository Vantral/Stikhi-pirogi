import telegrambotapi as telebot
from poet import Poem
from token import TOKEN

bot = telebot.TeleBot(TOKEN)
poem = Poem()


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text.lower() == "/gen":
        try:
            poem.generate()
            response = poem.show()
            bot.send_message(message.from_user.id, response)
            poem.clear()
        except:
            bot.send_message(message.from_user.id, "Произошла досадная оШиБкА.. попробуй ещё раз")


bot.polling(none_stop=True)
