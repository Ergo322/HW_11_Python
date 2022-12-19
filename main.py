import telebot
from telebot import types

TOKEN = "5879295672:AAE_eKUa3ecZl7nf74f13Qg08kPq_EpHMi0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def websity(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    contacts = types.KeyboardButton('Контакты')
    prays = types.KeyboardButton('Прайс-лист')
    markup.add(contacts, prays)
    bot.send_message(message.chat.id, "Выберите действие подходящее вам", reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Контакты':
        bot.send_message(message.chat.id, 'Наш администратор Егор https://t.me/ergo322 ответит на все ваши вопросы')
    elif message.text == 'Прайс-лист':
        prays_photo = open('Циркон.png', 'rb')
        bot.send_photo(message.chat.id, prays_photo)

bot.polling(none_stop=True)