import telebot, wikipedia
from telebot import types

token = '7184176667:AAEIye1y4KM_meqEagF2Yu0TAnun2PnFmSw'
bot = telebot.TeleBot(token)

wikipedia.set_lang('ru')

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Меню')
button2 = types.KeyboardButton('Книга жалоб')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start'])
def start(message):
    message2 = bot.send_message(message.chat.id, 'Привет! Я работник кафе!', reply_markup = keyboard)
    bot.register_next_step_handler(message2, handle_text)


def getwiki(word):
    try:
        wikitext = wikipedia.page(word).content[:500]
        wikitext = wikitext.split('. ')
        wikitext = '. '.join(wikitext[:-1]) + '.'
    except:
        wikitext = 'Об этом слове, нет информации'
    return wikitext


def handle_text(message):
    word = message.text # сообщение в чате текст
    info = getwiki(word)
    bot.send_message(message.chat.id, info, reply_markup=types.ReplyKeyboardRemove())




bot.polling(none_stop=True)




